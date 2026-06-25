# healthbar.py

health = 75
max_health = 100

bar_length = 20

filled = int(bar_length * health / max_health)

bar = "█" * filled + "-" * (bar_length - filled)

print(f"HP [{bar}] {health}/{max_health}")
