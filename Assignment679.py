
      import random

print("BRAIN TEASERS!!\n Instructions \n Enter Y to continue and Q to quit the game")
play = input("Do you want to play a game?")
if play == "y":
    print("Enter a three-digit number:")

try:
    digits = list(range(10))
    random.shuffle(digits)
    new_list = (digits[:3])
    print(new_list)

except ValueError:
    print("Ooooopss!!!!This is not a number.Please try again.'")


def my_game():
    y = 0
    for x in range(0, 3):
        if entry[x] in digits and entry[x] != digits[x]:
            y = 1
            print(f"Close {entry[x]}")

    if y != 1:
        c = 0
        for x in range(0, 3):
            if entry[x] == digits[x]:
                c = 1
                print(f"Match {entry[x]}")

        if c != 1:
            if entry != digits:
                print("Nope")


while True:
    entry = input("Enter a 3-digit number:")
    my_game()
