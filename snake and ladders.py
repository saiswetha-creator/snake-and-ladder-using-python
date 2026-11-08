
import random

print("================================")
print("       SNAKE AND LADDER")
print("================================")

input('Press ENTER to start the game...')

print("\nSelect Game Mode:")
print("1. Play with Friends")
print("2. Play with Computer")

choice = int(input("Enter your choice: "))

p1 = input("Enter Player 1 name: ")
p2 = input("Enter Player 2 name: ")

pos1 = 0
pos2 = 0

snakes = {
    17: 7,
    54: 34,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    99: 78
}

ladders = {
    4: 14,
    9: 31,
    20: 38,
    28: 84,
    40: 59,
    63: 81,
    71: 91
}

while pos1 < 100 and pos2 < 100:
    input("\n" + p1 + ", press ENTER to roll the dice")

    dice = random.randint(1, 6)
    print("Dice number:", dice)

    if pos1 + dice <= 100:
        pos1 = pos1 + dice

    print(p1, "is at position:", pos1)

    if pos1 in ladders:
        print("Congratulations! You got a ladder!")
        pos1 = ladders[pos1]
        print("Moved up to:", pos1)

    elif pos1 in snakes:
        print("Oh no! A snake!")
        pos1 = snakes[pos1]
        print("Moved down to:", pos1)

    if pos1 == 100:
        print("\nCongratulations!", p1, "WINS!")
        break

    if dice == 6:
        print("You rolled a 6! You get another turn.")
        continue

    input("\n" + p2 + ", press ENTER to roll the dice")

    dice = random.randint(1, 6)
    print("Dice number:", dice)

    if pos2 + dice <= 100:
        pos2 = pos2 + dice

    print(p2, "is at position:", pos2)

    if pos2 in ladders:
        print("Congratulations! You got a ladder!")
        pos2 = ladders[pos2]
        print("Moved up to:", pos2)

    elif pos2 in snakes:
        print("Oh no! A snake!")
        pos2 = snakes[pos2]
        print("Moved down to:", pos2)

    if pos2 == 100:
        print("\nCongratulations!", p2, "WINS!")
        break

    if dice == 6:
        print("You rolled a 6! You get another turn.")

print("\n========== GAME OVER ==========")
print("Thank you for playing!")
