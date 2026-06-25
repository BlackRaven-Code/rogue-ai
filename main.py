from pathlib import Path
import signal
import subprocess
import sys

from core.console import show_console_header, get_latest_session_log
from core.session_log import create_session_log
from game.hud import show_hud
from game.inventory import inventory
from game.missions import generate_mission

QUESTIONARY_UNAVAILABLE = False
QUESTIONARY_NOTICE_SHOWN = False


def _questionary_timeout(signum, frame):
    raise TimeoutError("questionary import timed out")


def get_questionary():
    global QUESTIONARY_UNAVAILABLE

    if QUESTIONARY_UNAVAILABLE:
        return None

    if sys.version_info >= (3, 14):
        QUESTIONARY_UNAVAILABLE = True
        return None

    previous_handler = signal.signal(signal.SIGALRM, _questionary_timeout)
    signal.alarm(2)

    try:
        import questionary
        return questionary

    except (ImportError, TimeoutError):
        QUESTIONARY_UNAVAILABLE = True
        return None

    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous_handler)


def select_menu(message, choices):
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        return select_numbered_menu(message, choices)

    questionary = get_questionary()

    if questionary:
        return questionary.select(message, choices=choices).ask()

    return select_numbered_menu(message, choices)


def select_numbered_menu(message, choices):
    global QUESTIONARY_NOTICE_SHOWN

    if not QUESTIONARY_NOTICE_SHOWN:
        print("\nNORA: Arrow-key menu unavailable. Switching to numbered input.")
        QUESTIONARY_NOTICE_SHOWN = True

    print(f"\n{message}")

    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")

    try:
        selected = input("\nSelect operation: ")
        selected_index = int(selected) - 1

        if 0 <= selected_index < len(choices):
            return choices[selected_index]

    except (ValueError, EOFError, KeyboardInterrupt):
        return None

    print("\nInvalid selection.")
    return None


def show_inventory():
    print("\nINVENTORY")
    print("-" * 20)

    for item in inventory:
        print(f"> {item}")


def show_git_status():
    print("\nGIT STATUS")
    print("-" * 20)

    try:
        result = subprocess.run(
            ["git", "status", "--short"],
            capture_output=True,
            text=True,
            timeout=5
        )

        output = result.stdout.strip() or result.stderr.strip()
        print(output or "Working tree clean.")

    except subprocess.TimeoutExpired:
        print("Command timed out.")


def get_python_files():
    files = []

    for path in Path(".").rglob("*.py"):
        path_parts = path.parts

        if "__pycache__" in path_parts or ".venv" in path_parts:
            continue

        files.append(str(path))

    return sorted(files)


def browse_python_files():
    files = get_python_files()

    if not files:
        print("\nNORA: No Python files detected.")
        return

    selected = select_menu(
        "NORA: Select Python file:",
        files + ["Back to Developer Console"]
    )

    if selected and selected != "Back to Developer Console":
        run_python_file(selected)


def run_python_file(file_path):
    if Path(file_path) == Path("main.py"):
        print("\nNORA: Black Raven OS is already running.")
        return

    print(f"\nNORA: Running {file_path}")
    print("-" * 40)

    try:
        subprocess.run([sys.executable, file_path], timeout=15)

    except subprocess.TimeoutExpired:
        print("\nNORA: Execution timed out after 15 seconds.")

    except KeyboardInterrupt:
        print("\nNORA: File execution interrupted.")

    except OSError as error:
        print(f"\nNORA: Unable to run file: {error}")


def developer_console():
    while True:
        choice = select_menu(
            "NORA Developer Console:",
            [
                "Create Session Log",
                "View Last Session Log",
                "Git Status",
                "Browse Python Files",
                "Back to Main Menu"
            ]
        )

        if choice == "Create Session Log":
            create_session_log()

        elif choice == "View Last Session Log":
            print(get_latest_session_log())

        elif choice == "Git Status":
            show_git_status()

        elif choice == "Browse Python Files":
            browse_python_files()

        elif choice == "Back to Main Menu" or choice is None:
            break

        input("\nPress Enter to continue...")


def main_menu():
    while True:
        show_console_header()

        choice = select_menu(
            "Select operation:",
            [
                "View HUD",
                "Generate Mission",
                "View Inventory",
                "Developer Console",
                "Exit"
            ]
        )

        if choice == "View HUD":
            show_hud()

        elif choice == "Generate Mission":
            generate_mission()

        elif choice == "View Inventory":
            show_inventory()

        elif choice == "Developer Console":
            developer_console()

        elif choice == "Exit" or choice is None:
            print("\nNORA: Disconnecting. Stay sharp, Commander.")
            break

        else:
            print("\nInvalid selection.")

        input("\nPress Enter to continue...")


main_menu()
