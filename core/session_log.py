import subprocess
from datetime import datetime
from pathlib import Path


def run_command(command):
    """Run a terminal command and return its output."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.stdout:
            return result.stdout.strip()
        if result.stderr:
            return result.stderr.strip()

        return "No output."

    except subprocess.TimeoutExpired:
        return f"Command timed out: {' '.join(command)}"


def create_session_log():
    today = datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    logs_folder = Path("logs")
    logs_folder.mkdir(exist_ok=True)

    log_file = logs_folder / f"session_{today}.txt"

    git_status = run_command(["git", "status", "--short"])
    git_diff = run_command(["git", "diff", "--stat"])
    recent_commits = run_command(["git", "--no-pager", "log", "--oneline", "-5"])

    content = f"""BLACK RAVEN OS SESSION LOG
==========================

Timestamp:
{timestamp}

GIT STATUS
----------
{git_status}

CHANGED FILES
-------------
{git_diff}

RECENT COMMITS
--------------
{recent_commits}

SESSION NOTES
-------------
Add manual notes here if needed.
"""

    with open(log_file, "w") as file:
        file.write(content)

    print(f"Session log created: {log_file}")
