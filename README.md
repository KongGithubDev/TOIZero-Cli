# TOI-ZERO Terminal Assistant

A professional CLI tool designed to automate the competitive programming workflow for the TOI-ZERO platform.

## Features

- **Task Management**: Initialize tasks with folder structure and code templates.
- **Unified Execution**: Run Python, C, and C++ solutions with flexible commands.
- **Automated Submission**: Submit code and track evaluation status in real-time.
- **Progress Tracking**: View completed tasks with scores from all categories.
- **Session Caching**: Automatic login session persistence (no repeated logins).

## Installation

1. Clone the repository into your local workspace.
2. Install dependencies:
   ```bash
   py -m pip install requests beautifulsoup4 python-dotenv
   ```
3. Configure credentials: Create a `.env` file in the root directory:
   ```env
   TOI_USERNAME=your_username
   TOI_PASSWORD=your_password
   ```

## Usage

Use the `toi` command from the project folder:

### Windows PowerShell
```powershell
.\toi <command> [args]
```

### Command Reference

#### `list [category]` - List all available tasks
Show all problems grouped by category with your completion status:
```bash
.\toi list              # Show all categories with progress
.\toi list A1          # Show only A1 tasks
.\toi list A2          # Show only A2 tasks
```
Output shows:
- ✓ Task [100/100] - Completed
- ✗ Task [50/100] - Attempted but not full score
- Task - Not attempted
- Progress summary per category

#### `start <task_id>` - Initialize task workspace
Create folder structure, code templates, and download problem PDF:
```bash
.\toi start A1-001
```

Creates:
```
solutions/
  A1-001/
    main.py      # Python template with input handling
    main.c       # C template
    main.cpp     # C++ template with fast I/O
tasks/
  A1-001.pdf     # Problem statement (auto-opened in IDE)
```

Also displays:
- Task title
- Type (Batch/Interactive)
- Time limit
- Memory limit
- Compilation commands for each language

#### `run <path>` or `run <task> <ext/file>` - Run solution
Multiple ways to run your code:
```bash
# Run by full path
.\toi run solutions/A1-001/main.cpp

# Run by task and extension (auto-finds file)
.\toi run A1-001 cpp     # Finds and runs first .cpp file
.\toi run A1-001 py      # Finds and runs first .py file
.\toi run A1-001 c       # Finds and runs first .c file

# Run by task and specific filename
.\toi run A1-001 main.cpp
.\toi run A1-001 mysolution.py
```

#### `submit <folder>` or `submit <task> <ext/file>` - Submit solution
Multiple ways to submit:
```bash
# Submit by folder (auto-finds solution file)
.\toi submit solutions/A1-001
.\toi submit A1-001

# Submit by task and extension
.\toi submit A1-001 cpp    # Submits first .cpp file
.\toi submit A1-001 py     # Submits first .py file

# Submit specific file
.\toi submit A1-001 main.cpp
.\toi submit A1-001 mycode.py
```

After submission:
- Waits for compilation/evaluation
- Shows real-time status updates
- Displays final score

#### `status <task_id>` - Check submission status
View latest submission results:
```bash
.\toi status A1-001
```

## Project Structure

```
TOI-ZERO/
├── toi.py              # Main CLI tool
├── toi.cmd             # Windows command wrapper
├── .env                # Credentials (ignored by git)
├── .session            # Cached login session (ignored by git)
├── .gitignore          # Git ignore rules
├── README.md           # This file
├── solutions/          # Your task workspaces
│   ├── A1-001/
│   │   ├── main.py
│   │   ├── main.c
│   │   └── main.cpp
│   └── A1-002/
└── tasks/              # Downloaded problem PDFs
    ├── A1-001.pdf
    └── A1-002.pdf
```

## Example Workflow

```powershell
# 1. View available tasks
.\toi list A1

# 2. Start working on A1-001
.\toi start A1-001
# - Creates folder with templates
# - Downloads PDF
# - Opens PDF in your IDE

# 3. Edit solutions/A1-001/main.cpp

# 4. Test your solution
.\toi run A1-001 cpp
# Enter test input: Watcharapong Namsaeng
# Verify output: Hello Watcharapong Namsaeng / WaNa

# 5. Submit to platform
.\toi submit A1-001 cpp
# Wait for evaluation...
# Score: 100 / 100

# 6. Check progress
.\toi list A1
# Shows ✓ A1-001 [100/100]
```

## Session Management

The tool automatically:
- Saves login session to `.session` file
- Reuses session on subsequent commands (no repeated logins)
- Refreshes session when expired

---
Developed for TOI-ZERO Competitive Programming.
