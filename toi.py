import os
import sys
import json
import re
import subprocess
import time

# Optional dependencies for web
try:
    import requests
    from bs4 import BeautifulSoup
    from dotenv import load_dotenv
    HAS_WEB_DEPS = True
except ImportError:
    HAS_WEB_DEPS = False


BASE_URL = "https://toi-coding.informatics.buu.ac.th/00-pre-toi"

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def run_solution(filename):
    if not os.path.exists(filename):
        sol_path = os.path.join("solutions", filename)
        if os.path.exists(sol_path):
            filename = sol_path
        else:
            print(f"{Colors.RED}Error: File {filename} not found.{Colors.RESET}")
            return None
    
    ext = filename.split('.')[-1]
    name = os.path.basename(filename).split('.')[0]
    
    try:
        if ext == 'py':
            cmd = ['python', filename]
            print(f"{Colors.CYAN}Running Python program...{Colors.RESET}")
            try:
                subprocess.run(cmd, capture_output=False, text=True)
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}Program interrupted.{Colors.RESET}")
            return None  # Already executed
        elif ext in ['c', 'cpp']:
            # Create exe in temp location
            import tempfile
            temp_dir = tempfile.gettempdir()
            out_file = os.path.join(temp_dir, name + '.exe' if os.name == 'nt' else name + '.out')
            compiler = 'gcc' if ext == 'c' else 'g++'
            compile_cmd = [compiler, filename, '-o', out_file]
            
            # Add UTF-8 support for g++
            if ext == 'cpp':
                compile_cmd.extend(['-finput-charset=UTF-8', '-fexec-charset=UTF-8'])
                
            cp = subprocess.run(compile_cmd, capture_output=True, text=True)
            if cp.returncode != 0:
                print(f"{Colors.RED}Compilation Error:{Colors.RESET}\n{cp.stderr}")
                return "COMP_ERR"
            
            # Run with input/output connected to console
            print(f"{Colors.CYAN}Running compiled program...{Colors.RESET}")
            try:
                subprocess.run([out_file], capture_output=False, text=True)
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}Program interrupted.{Colors.RESET}")
            # Cleanup exe file
            if os.path.exists(out_file):
                try:
                    os.remove(out_file)
                except:
                    pass
            return None  # Already executed
    except Exception as e:
        print(f"{Colors.RED}Execution Error: {e}{Colors.RESET}")
        return None

SESSION_FILE = ".session"

def save_session(session):
    """Save session cookies to file."""
    try:
        with open(SESSION_FILE, 'w') as f:
            json.dump(dict(session.cookies), f)
    except:
        pass

def load_session():
    """Load session cookies from file."""
    try:
        if os.path.exists(SESSION_FILE):
            with open(SESSION_FILE, 'r') as f:
                cookies = json.load(f)
                session = requests.Session()
                session.cookies.update(cookies)
                return session
    except:
        pass
    return None

def test_session(session):
    """Test if session is still valid."""
    try:
        r = session.get(BASE_URL, timeout=5)
        return "Logout" in r.text
    except:
        return False

def get_session():
    if not HAS_WEB_DEPS:
        print(f"{Colors.RED}Error: Missing requests or beautifulsoup4.{Colors.RESET}")
        return None
    
    # Try to load existing session first
    session = load_session()
    if session and test_session(session):
        return session
    
    # Need to login
    load_dotenv()
    user = os.getenv("TOI_USERNAME")
    pw = os.getenv("TOI_PASSWORD")
    if not user or not pw:
        print(f"{Colors.RED}Error: No credentials in .env{Colors.RESET}")
        return None
    
    print(f"{Colors.CYAN}Logging in...{Colors.RESET}")
    session = requests.Session()
    r = session.get(BASE_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find('input', {'name': '_xsrf'})
    
    data = {"username": user, "password": pw}
    if csrf: data["_xsrf"] = csrf['value']
    
    r = session.post(f"{BASE_URL}/login", data=data, allow_redirects=True)
    if "Logout" not in r.text:
        print(f"{Colors.RED}Login failed.{Colors.RESET}")
        return None
    
    # Save session for reuse
    save_session(session)
    return session

def list_tasks(category_filter=None):
    """List all available tasks from the main page table with scores and titles."""
    session = get_session()
    if not session: return
    
    print(f"{Colors.CYAN}Fetching task list from {BASE_URL}...{Colors.RESET}")
    r = session.get(f"{BASE_URL}")
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Parse task table for IDs, titles, and scores from main page (single request)
    task_info = {}  # task_id -> {title, time, memory, score}
    table = soup.find('table', class_='table')
    if table:
        for row in table.find_all('tr')[1:]:  # Skip header
            tds = row.find_all('td')
            th = row.find('th')
            if th and len(tds) >= 5:
                task_id = th.text.strip()
                if re.match(r'[A-Z]\d+-\d+', task_id):
                    # Score is in first td (e.g., "0 / 100" or "100 / 100")
                    score_text = tds[0].text.strip() if len(tds) > 0 else ''
                    score_match = re.search(r'(\d+)\s*/\s*\d+', score_text)
                    score = int(score_match.group(1)) if score_match else None
                    
                    # Title is in 3rd td (index 2)
                    title = tds[2].text.strip() if len(tds) > 2 else ''
                    # Time limit is in 4th td (index 3)
                    time_limit = tds[3].text.strip() if len(tds) > 3 else ''
                    # Memory limit is in 5th td (index 4)
                    memory_limit = tds[4].text.strip() if len(tds) > 4 else ''
                    
                    task_info[task_id] = {
                        'title': title,
                        'time': time_limit,
                        'memory': memory_limit,
                        'score': score
                    }
    
    if not task_info:
        print(f"{Colors.YELLOW}No tasks found.{Colors.RESET}")
        return
    
    # Group by category (A1, A2, A3, etc.)
    from collections import defaultdict
    grouped = defaultdict(list)
    for task in sorted(task_info.keys()):
        category = task.split('-')[0]
        grouped[category].append(task)
    
    # Filter by category if specified
    if category_filter:
        if category_filter not in grouped:
            print(f"\n{Colors.YELLOW}No tasks found in category '{category_filter}'.{Colors.RESET}")
            available = ', '.join(sorted(grouped.keys())[:10]) + ('...' if len(grouped) > 10 else '')
            print(f"Available categories: {available}")
            return
        categories_to_show = [category_filter]
    else:
        categories_to_show = sorted(grouped.keys())
    
    print(f"\n{Colors.BOLD}Available Tasks:{Colors.RESET}")
    total_tasks = len(task_info)
    completed_tasks = sum(1 for info in task_info.values() if info.get('score') == 100)
    
    for category in categories_to_show:
        if category not in grouped:
            continue
        print(f"\n{Colors.CYAN}{category}:{Colors.RESET}")
        for task in sorted(grouped[category]):
            info = task_info.get(task, {})
            title = info.get('title', '')
            score = info.get('score')
            title_display = f" - {title}" if title else ''
            
            if score == 100:
                print(f"  {Colors.GREEN}✓ {task}{title_display} [{score}/100]{Colors.RESET}")
            elif score is not None and score > 0:
                print(f"  {Colors.YELLOW}◐ {task}{title_display} [{score}/100]{Colors.RESET}")
            else:
                # Unfinished (0 or None) - show in white without score
                print(f"  {task}{title_display}")
        cat_completed = sum(1 for t in grouped[category] if task_info.get(t, {}).get('score') == 100)
        cat_partial = sum(1 for t in grouped[category] if (task_info.get(t, {}).get('score') or 0) > 0 and task_info.get(t, {}).get('score') != 100)
        progress_text = f"{cat_completed}/{len(grouped[category])} completed"
        if cat_partial > 0:
            progress_text += f" ({cat_partial} partial)"
        print(f"  {Colors.BOLD}Progress: {progress_text}{Colors.RESET}")
    
    if not category_filter:
        print(f"\n{Colors.BOLD}Total Progress: {completed_tasks}/{total_tasks} tasks completed ({completed_tasks*100//total_tasks}%){Colors.RESET}")

def start_task(task_id):
    """Initialize task workspace: create folder, templates, and download PDF."""
    session = get_session()
    if not session: return
    print(f"{Colors.CYAN}Starting {task_id}...{Colors.RESET}")
    
    # Create solutions folder structure
    task_folder = f"solutions/{task_id}"
    os.makedirs(task_folder, exist_ok=True)
    print(f"  Created folder: {task_folder}/")
    
    # Create template files
    templates = {
        "main.py": '''# Python solution for {}
import sys

def main():
    # Read input
    data = sys.stdin.read().split()
    # Your code here
    
if __name__ == "__main__":
    main()
'''.format(task_id),
        "main.c": '''// C solution for {}
#include <stdio.h>

int main() {{
    // Read input
    // Your code here
    
    return 0;
}}
'''.format(task_id),
        "main.cpp": '''// C++ solution for {}
#include <bits/stdc++.h>
using namespace std;

int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    // Read input
    // Your code here
    
    return 0;
}}
'''.format(task_id)
    }
    
    for filename, content in templates.items():
        filepath = f"{task_folder}/{filename}"
        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  Created template: {filepath}")
    
    # Download PDF
    pdf_url = f"{BASE_URL}/tasks/{task_id}/attachments/{task_id}.pdf"
    r = session.get(pdf_url)
    if r.status_code == 200:
        os.makedirs("tasks", exist_ok=True)
        path = f"tasks/{task_id}.pdf"
        with open(path, "wb") as f: f.write(r.content)
        print(f"  Downloaded PDF to {path}")
    
    # Extract info from description page
    r = session.get(f"{BASE_URL}/tasks/{task_id}/description")
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Extract and print problem title from h1
    h1 = soup.find('h1')
    if h1:
        title_text = h1.get_text().replace('description', '').strip()
        print(f"\n{Colors.BOLD}{Colors.CYAN}{title_text}{Colors.RESET}")
    
    # Print task details from table
    print(f"\n{Colors.BOLD}Task Info:{Colors.RESET}")
    table = soup.find('table', class_='table')
    if table:
        rows = table.find_all('tr')
        current_key = None  # Track rowspan th
        for row in rows:
            th = row.find('th')
            tds = row.find_all('td')
            # Update current_key if th exists
            if th:
                current_key = th.text.strip()
                # Check for rowspan to remember this key
                rowspan = th.get('rowspan')
                if rowspan:
                    current_key = th.text.strip()
            # Process row if we have a key and td cells
            if current_key and tds:
                if len(tds) == 1:
                    val = tds[0].text.strip()
                    print(f"  {current_key}: {val}")
                elif len(tds) >= 2:
                    lang = tds[0].text.strip()
                    cmd = tds[1].text.strip()[:60]
                    print(f"  {current_key} ({lang}): {cmd}...")
    
def submit_task(task_folder, specific_file=None):
    """Submit solution from task folder. Folder name is the task_id."""
    # Handle both folder path and direct file path (for backward compatibility)
    if os.path.isfile(task_folder):
        # Legacy mode: direct file submission
        filename = task_folder
        task_id = os.path.basename(filename).split('.')[0]
    else:
        # New mode: folder submission
        # Normalize path
        task_folder = task_folder.rstrip('/\\')
        task_id = os.path.basename(task_folder)
        
        if specific_file:
            # Specific file requested (e.g., submit A1-001 main.cpp)
            filepath = os.path.join(task_folder, specific_file)
            if os.path.exists(filepath):
                filename = filepath
                print(f"{Colors.CYAN}Submitting: {specific_file}{Colors.RESET}")
            else:
                print(f"{Colors.RED}Error: File {filepath} not found.{Colors.RESET}")
                return
        else:
            # Auto-find solution file in folder
            solution_file = None
            for ext in ['.py', '.cpp', '.c']:
                for f in os.listdir(task_folder):
                    if f.endswith(ext):
                        solution_file = os.path.join(task_folder, f)
                        break
                if solution_file:
                    break
            
            if not solution_file:
                print(f"{Colors.RED}Error: No solution file (.py, .cpp, .c) found in {task_folder}/{Colors.RESET}")
                return
            
            filename = solution_file
            print(f"{Colors.CYAN}Found solution: {os.path.basename(filename)}{Colors.RESET}")
    
    if not os.path.exists(filename):
        print(f"{Colors.RED}Error: File {filename} not found.{Colors.RESET}")
        return
    
    session = get_session()
    if not session: return
    
    print(f"{Colors.CYAN}Submitting {task_id}...{Colors.RESET}")
    submit_url = f"{BASE_URL}/tasks/{task_id}/submit"
    r = session.get(f"{BASE_URL}/tasks/{task_id}/submissions")
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find('input', {'name': '_xsrf'})
    
    ext = filename.split('.')[-1]
    lang_map = {'py': 'Python 3 / CPython', 'c': 'C11 / gcc', 'cpp': 'C++17 / g++'}
    
    with open(filename, 'rb') as f:
        files = {f"{task_id}.%l": f}
        data = {'language': lang_map.get(ext, 'Python 3')}
        if csrf: data['_xsrf'] = csrf['value']
        headers = {'Referer': f"{BASE_URL}/tasks/{task_id}/submissions", 'Origin': BASE_URL}
        r = session.post(submit_url, data=data, files=files, headers=headers)
        if r.status_code in [200, 302]:
            print(f"{Colors.GREEN}Submission accepted!{Colors.RESET}")
            poll_status(task_id, None, session)
        else:
            print(f"{Colors.RED}Submission failed: HTTP {r.status_code}{Colors.RESET}")

def show_submission_details(details_url, session):
    """Fetch and display detailed submission info from details page."""
    try:
        r = session.get(details_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Parse test cases
        testcase_table = soup.find('table', class_='testcase-list')
        if testcase_table:
            print(f"\n{Colors.BOLD}Submission details{Colors.RESET}")
            print(f"{'#':<4} {'Outcome':<12} Details")
            print("-" * 40)
            for row in testcase_table.find_all('tr')[1:]:  # Skip header
                tds = row.find_all('td')
                if len(tds) >= 3:
                    idx = tds[0].text.strip()
                    outcome = tds[1].text.strip()
                    details = tds[2].text.strip()
                    outcome_color = Colors.GREEN if outcome == "Correct" else Colors.RED if outcome in ["Wrong", "Failed"] else Colors.YELLOW
                    print(f"{idx:<4} {outcome_color}{outcome:<12}{Colors.RESET} {details}")
        
        # Parse compilation output
        comp_heading = soup.find('h3', string=lambda x: x and 'Compilation output' in x)
        if comp_heading:
            print(f"\n{Colors.BOLD}Compilation output{Colors.RESET}")
            all_tables = comp_heading.find_all_next('table', class_='table')
            for ti, comp_table in enumerate(all_tables[:1]):
                # Handle malformed HTML where th/td may be outside tr
                tbody = comp_table.find('tbody') or comp_table
                all_ths = tbody.find_all('th')
                for th in all_ths:
                    # Find next sibling td (may not be in same tr)
                    td = th.find_next_sibling('td')
                    if td:
                        label = th.text.strip()
                        value = td.text.strip()
                        print(f"{label} {value}")
            
            # Standard output
            stdout_heading = comp_heading.find_next('h4', string=lambda x: x and 'Standard output' in x)
            if stdout_heading:
                pre = stdout_heading.find_next('pre')
                stdout = pre.text.strip() if pre else ""
                if stdout:
                    print(f"\n{Colors.BOLD}Standard output{Colors.RESET}")
                    print(stdout)
            
            # Standard error
            stderr_heading = comp_heading.find_next('h4', string=lambda x: x and 'Standard error' in x)
            if stderr_heading:
                pre = stderr_heading.find_next('pre')
                stderr = pre.text.strip() if pre else ""
                if stderr:
                    print(f"\n{Colors.BOLD}Standard error{Colors.RESET}")
                    print(stderr)
    except Exception as e:
        pass  # Silently skip if details fetch fails

def poll_status(task_id, sub_id, session):
    print("Waiting for results...", end="", flush=True)
    pending_statuses = ["Queued", "Compiling", "Running", "Evaluating"]
    submission_id = None
    for _ in range(30):  # Increased to 60 seconds max wait
        time.sleep(2)
        print(".", end="", flush=True)
        r = session.get(f"{BASE_URL}/tasks/{task_id}/submissions")
        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.find_all('tr')
        if len(rows) > 1:
            first_row = rows[1]
            cols = first_row.find_all('td')
            status = cols[1].text.strip()
            # Check if status starts with any pending status (handles "Compiling..." etc.)
            is_pending = any(status.startswith(s) for s in pending_statuses)
            if not is_pending:
                print(f"\nLast Submission: {cols[0].text.strip()}")
                print(f"Status: {status.replace('details', '').strip()}")
                print(f"{Colors.BOLD}Score: {cols[2].text.strip()}{Colors.RESET}")
                # Get submission ID from data-submission attribute
                submission_id = first_row.get('data-submission')
                break
    else:
        print("\nStill processing. Check 'py toi.py status " + task_id + "' later.")
        return
    
    # Fetch and display detailed submission info
    if submission_id:
        details_url = f"{BASE_URL}/tasks/{task_id}/submissions/{submission_id}/details"
        show_submission_details(details_url, session)

def get_status_detailed(task_id, session):
    """Get status with full details without waiting animation."""
    r = session.get(f"{BASE_URL}/tasks/{task_id}/submissions")
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('tr')
    if len(rows) > 1:
        # Get submission ID from data-submission attribute
        first_row = rows[1]
        submission_id = first_row.get('data-submission')
        
        cols = first_row.find_all('td')
        if len(cols) >= 3:
            print(f"Last Submission: {cols[0].text.strip()}")
            status = cols[1].text.strip()
            print(f"Status: {status.replace('details', '').strip()}")
            print(f"{Colors.BOLD}Score: {cols[2].text.strip()}{Colors.RESET}")
            
            if submission_id:
                details_url = f"{BASE_URL}/tasks/{task_id}/submissions/{submission_id}/details"
                show_submission_details(details_url, session)
            else:
                print("Debug: No submission ID found")
        else:
            print(f"{Colors.YELLOW}No submissions found for {task_id}{Colors.RESET}")
    else:
        print(f"{Colors.YELLOW}No submissions found for {task_id}{Colors.RESET}")

def open_pdf_in_ide(pdf_path):
    """Open PDF file in the current IDE/editor."""
    # Detect IDE from environment and try appropriate command
    editors = []
    
    # Check for Windsurf
    if os.getenv('WINDSURF_VERSION') or os.getenv('WINDSURF_ENV'):
        editors.append('windsurf')
    
    # Check for Cursor
    if os.getenv('CURSOR_PATH') or os.getenv('CURSOR_VERSION'):
        editors.append('cursor')
    
    # Check for VSCode
    if os.getenv('VSCODE_CWD') or os.getenv('VSCODE_PID'):
        editors.append('code')
    
    # Default fallback order
    editors.extend(['windsurf', 'cursor', 'code'])
    
    for editor in editors:
        try:
            result = subprocess.run([editor, pdf_path], shell=True, capture_output=True)
            if result.returncode == 0:
                print(f"  Opened in {editor}: {pdf_path}")
                return
        except:
            continue
    
    print(f"  PDF saved to: {pdf_path}")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or (args[0] not in ['list'] and len(args) < 2):
        print("Usage: py toi.py [list|run|start|submit|status] <task_id/file>")
        print("  list [category] - List all available tasks (e.g., list A1)")
        print("  run <path>      - Run solution file (e.g., run solutions/A1-001/main.cpp)")
        print("  run <task> <file> - Run from folder (e.g., run A1-001 main.cpp)")
        print("  run <task> <ext>- Run by extension (e.g., run A1-001 cpp/py/c)")
        print("  start <task_id> - Create task folder, templates, and download PDF")
        print("  submit <folder> - Submit from folder (auto-find file)")
        print("  submit <task> <file> - Submit specific file (e.g., submit A1-001 main.cpp)")
        print("  status <task_id> - Check submission status")
    elif args[0] == "list":
        category = args[1] if len(args) > 1 else None
        list_tasks(category)
    elif args[0] == "run":
        # Support multiple formats:
        #   run solutions/A1-001/main.cpp
        #   run A1-001 main.cpp
        #   run A1-001 cpp (find first .cpp file)
        arg = args[1]
        if len(args) >= 3:
            # Format: run A1-001 main.cpp  or  run A1-001 cpp
            task_id = arg
            file_arg = args[2]
            task_folder = f"solutions/{task_id}"
            
            if not os.path.exists(task_folder):
                print(f"{Colors.RED}Error: Folder {task_folder} not found. Run: toi start {task_id}{Colors.RESET}")
            elif not file_arg.startswith('main.'):
                # Format: run A1-001 cpp  (find by extension)
                ext = file_arg if file_arg.startswith('.') else '.' + file_arg
                found = False
                for f in os.listdir(task_folder):
                    if f.endswith(ext):
                        run_solution(os.path.join(task_folder, f))
                        found = True
                        break
                if not found:
                    print(f"{Colors.RED}Error: No *{ext} file found in {task_folder}/{Colors.RESET}")
            else:
                # Format: run A1-001 main.cpp
                filepath = os.path.join(task_folder, file_arg)
                if os.path.exists(filepath):
                    run_solution(filepath)
                else:
                    print(f"{Colors.RED}Error: File {filepath} not found.{Colors.RESET}")
        else:
            # Format: run solutions/A1-001/main.cpp  or  run A1-001.cpp
            run_solution(arg)
    elif args[0] == "start":
        start_task(args[1])
        pdf_path = f"tasks/{args[1]}.pdf"
        if os.path.exists(pdf_path):
            open_pdf_in_ide(pdf_path)
    elif args[0] == "submit":
        # Support multiple formats:
        #   submit solutions/A1-001  (auto-find file)
        #   submit A1-001 main.cpp   (specific file)
        #   submit A1-001 cpp        (find by extension)
        if len(args) >= 3:
            task_id = args[1]
            file_arg = args[2]
            task_folder = f"solutions/{task_id}"
            
            if not file_arg.startswith('main.') and not file_arg.startswith('.'):
                # Format: submit A1-001 cpp (find by extension)
                ext = '.' + file_arg
                found_file = None
                if os.path.exists(task_folder):
                    for f in os.listdir(task_folder):
                        if f.endswith(ext):
                            found_file = f
                            break
                if found_file:
                    submit_task(task_folder, found_file)
                else:
                    print(f"{Colors.RED}Error: No *{ext} file found in {task_folder}/{Colors.RESET}")
            else:
                # Format: submit A1-001 main.cpp
                submit_task(task_folder, file_arg)
        else:
            # Format: submit solutions/A1-001  or  submit A1-001
            arg = args[1]
            if not arg.startswith('solutions/'):
                arg = f"solutions/{arg}"
            submit_task(arg)
    elif args[0] == "status":
        s = get_session()
        if s: get_status_detailed(args[1], s)
