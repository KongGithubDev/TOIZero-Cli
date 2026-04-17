# TOI-ZERO Terminal Assistant

A professional CLI tool designed to automate the competitive programming workflow for the TOI-ZERO platform.

## Features

- Unified Execution: Run Python, C, and C++ solutions with a single command.
- Task Pulling: Download problem PDF and display task info (Type, Time/Memory limits, Compilation commands). Auto-opens PDF in IDE.
- Automated Submission: Submit code and track evaluation status in real-time.
- Status Polling: Check latest submission scores and platform status.

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

### Using the `toi` command

Use the short `toi` command instead of `python toi.py`:

**Add to PATH (One-time setup):**
1. Copy the path to this folder (e.g., `C:\Users\...\TOI-ZERO`)
2. Add to your system PATH environment variable
3. Restart your terminal

Or just use from the project folder directly.

### List All Tasks
Show all available problems grouped by category (A1, A2, A3, etc.):
```bash
toi list
```

### 1. Fetch Task Data
Download problem PDF and display task information (Type, Time limit, Memory limit, Compilation commands). Auto-opens PDF in your IDE:
```bash
toi pull A1-001
```

### 2. Run Solution
Execute your code with interactive manual input:
```bash
toi run A1-001.py
```

### 3. Submit to Platform
Submit your code and watch the live grading progress:
```bash
toi submit A1-001.py
```

### 4. Check Grade Status
Check the latest results for a specific task:
```bash
toi status A1-001
```

## Project Structure

- `toi.py`: The main CLI tool logic.
- `solutions/`: Folder for your solution files (e.g., `A1-001.py`, `A1-002.cpp`).
- `tasks/`: Directory containing downloaded problem PDFs.
- `.env`: Secure storage for your credentials (ignored by git).
- `.session`: Cached session cookies (auto-created, ignored by git).

---
Developed for TOI-ZERO Competitive Programming.
