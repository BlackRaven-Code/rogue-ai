# damage.py

import time

health = 100

while health > 0:

    bar = "█" * (health // 5)

    print(f"\rHP [{bar:<20}] {health}", end="")

    health -= 5

    time.sleep(0.15)

print("\nPlayer Down")
