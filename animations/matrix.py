# matrix.py

import random
import time

chars = "01"

while True:

    line = ""

    for _ in range(80):
        line += random.choice(chars)

    print(line)

    time.sleep(0.05)
