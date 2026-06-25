import random

targets = [
    "Corporate Courier",
    "Data Broker",
    "Security Drone",
    "Gang Lieutenant",
    "TitanCore Operative"
]

locations = [
    "Sector 12",
    "Industrial Zone",
    "Neural Labs",
    "Old Metro Station",
    "Data Vault"
]

rewards = [
    25,
    50,
    75,
    100
]

def generate_mission():

    target = random.choice(targets)
    location = random.choice(locations)
    reward = random.choice(rewards)

    print("\n========================")
    print("MISSION RECEIVED")
    print("========================")

    print(f"\nTarget: {target}")
    print(f"Location: {location}")
    print(f"Reward: +{reward} XP")

    choice = input("\nAccept Mission? (Y/N): ")

    if choice.lower() == "y":
        print("\nMission Accepted.")
    else:
        print("\nMission Declined.")
