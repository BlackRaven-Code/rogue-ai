# scanner.py

import time

frames = ["|", "/", "-", "\\"]

for i in range(30):
    print("\rScanning " + frames[i % 4], end="")
    time.sleep(0.1)

print("\nTarget Found")
