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
            return subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
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
            result = subprocess.run([out_file], capture_output=False, text=True)
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

def pull_task(task_id):
    session = get_session()
    if not session: return
    print(f"{Colors.CYAN}Fetching {task_id}...{Colors.RESET}")
    
    # Download PDF
    pdf_url = f"{BASE_URL}/tasks/{task_id}/attachments/{task_id}.pdf"
    r = session.get(pdf_url)
    if r.status_code == 200:
        os.makedirs("tasks", exist_ok=True)
        path = f"tasks/{task_id}.pdf"
        with open(path, "wb") as f: f.write(r.content)
        print(f"Downloaded PDF to {path}")
    
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
    
def submit_task(filename):
    if not os.path.exists(filename):
        sol_path = os.path.join("solutions", filename)
        if os.path.exists(sol_path):
            filename = sol_path
        else:
            print(f"{Colors.RED}Error: File {filename} not found.{Colors.RESET}")
            return
    task_id = os.path.basename(filename).split('.')[0]
    session = get_session()
    if not session: return
    
    print(f"{Colors.CYAN}Submitting {filename}...{Colors.RESET}")
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

def poll_status(task_id, sub_id, session):
    print("Waiting for results...", end="", flush=True)
    pending_statuses = ["Queued", "Compiling", "Running", "Evaluating"]
    for _ in range(30):  # Increased to 60 seconds max wait
        time.sleep(2)
        print(".", end="", flush=True)
        r = session.get(f"{BASE_URL}/tasks/{task_id}/submissions")
        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.find_all('tr')
        if len(rows) > 1:
            cols = rows[1].find_all('td')
            status = cols[1].text.strip()
            # Check if status starts with any pending status (handles "Compiling..." etc.)
            is_pending = any(status.startswith(s) for s in pending_statuses)
            if not is_pending:
                print(f"\nLast Submission: {cols[0].text.strip()}")
                print(f"Status: {status}")
                print(f"{Colors.BOLD}Score: {cols[2].text.strip()}{Colors.RESET}")
                return
    print("\nStill processing. Check 'py toi.py status " + task_id + "' later.")

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
    if not args or len(args) < 2:
        print("Usage: py toi.py [run|pull|submit|status] <task_id/file>")
        print("  run <file>      - Run solution (Python/C/C++)")
        print("  pull <task_id>  - Fetch problem PDF and info")
        print("  submit <file>   - Submit solution to platform")
        print("  status <task_id> - Check submission status")
    elif args[0] == "run":
        run_solution(args[1])
    elif args[0] == "pull":
        pull_task(args[1])
        pdf_path = f"tasks/{args[1]}.pdf"
        if os.path.exists(pdf_path):
            open_pdf_in_ide(pdf_path)
    elif args[0] == "submit": submit_task(args[1])
    elif args[0] == "status":
        s = get_session()
        if s: poll_status(args[1], None, s)
