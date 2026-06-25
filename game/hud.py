import time
import os

body = 15
reflex = 12
xp = 100

from game.inventory import inventory

def clear():
    os.system("clear")

def show_hud():
    clear()

    print("\033[95m" + "=" * 35)
    print("      ROGUE AI SYSTEM")
    print("=" * 35 + "\033[0m")

    print(f"\033[96mBODY   : {body}\033[0m")
    print(f"\033[96mREFLEX : {reflex}\033[0m")
    print(f"\033[93mXP     : {xp}\033[0m")

    print("\n\033[92mInventory\033[0m")

    for item in inventory:
        print(f"> {item}")

    print("\n\033[92mStatus: ONLINE\033[0m")

    time.sleep(1)
