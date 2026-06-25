import os
import time
import random

ghost = [
    " .-. ",
    "(o o)",
    "| O |",
    "|   |",
    "'~~~'"
]

while True:

    os.system("clear")

    x = random.randint(0, 60) 
    y = random.randint(0, 15)

    print("\n" * y)

    for line in ghost:
        print("\033[92m" + (" "* x + line) + "\033[0m")

    time.sleep(.2)
