from pathlib import Path
import subprocess


def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.stdout:
            return result.stdout.strip()
        if result.stderr:
            return result.stderr.strip()

        return "No output."

    except subprocess.TimeoutExpired:
        return "Command timed out."


def get_git_status_summary():
    status = run_command(["git", "status", "--short"])

    if status == "No output.":
        return "Working tree clean."

    lines = status.splitlines()
    return f"{len(lines)} file(s) modified or untracked."


def get_latest_session_log():
    logs_folder = Path("logs")

    if not logs_folder.exists():
        return "No logs folder found."

    session_logs = sorted(logs_folder.glob("session_*.txt"))

    if not session_logs:
        return "No session logs found."

    latest_log = session_logs[-1]

    with open(latest_log, "r") as file:
        return file.read()


def show_console_header():
    print("=" * 40)
    print("BLACK RAVEN OS v0.1")
    print("=" * 40)

    print("\nNORA: Good evening, Commander.")
    print("\nProject Status:")
    print(get_git_status_summary())

    print("\nCurrent Objective:")
    print("Recover the XP Module")
