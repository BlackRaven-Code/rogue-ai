from console import show_console_header, get_latest_session_log
from missions import generate_mission
from session_log import create_session_log
from hud import show_hud
from inventory import inventory


def show_inventory():
    print("\nINVENTORY")
    print("-" * 20)

    for item in inventory:
        print(f"> {item}")


def main_menu():
    while True:
        show_console_header()

        print("\n1. View HUD")
        print("2. Generate Mission")
        print("3. View Inventory")
        print("4. Create Session Log")
        print("5. View Last Session Log")
        print("6. Exit")

        choice = input("\nSelect operation: ")

        if choice == "1":
            show_hud()

        elif choice == "2":
            generate_mission()

        elif choice == "3":
            show_inventory()

        elif choice == "4":
            create_session_log()

        elif choice == "5":
            print(get_latest_session_log())

        elif choice == "6":
            print("\nNORA: Disconnecting. Stay sharp, Commander.")
            break

        else:
            print("\nInvalid selection.")

        input("\nPress Enter to continue...")


main_menu()

