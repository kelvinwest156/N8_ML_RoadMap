import random


def roll_dice():
    roll = random.randint(1, 6)
    print(f"{count} roll(s).\nYou rolled {roll}")


count = 1
while input("Roll the dice: ") == "r":
    roll_dice()
    print()
    count = count + 1
print("Simulator ended")
