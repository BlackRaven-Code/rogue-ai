import questionary
from pathlib import Path


def get_python_files():
    files = []

    for path in Path(".").rglob("*.py"):
        if "__pycache__" not in str(path):
            files.append(str(path))

    return sorted(files)


def main():
    selected = questionary.select(
        "Choose a Python file:",
        choices=get_python_files()
    ).ask()

    print(f"\nYou selected:\n{selected}")


if __name__ == "__main__":
    main()
