
import random

digits = list(range(10))
random.shuffle(digits)
new_list = (digits[:3])
print(new_list)

print("BRAIN TEASERS!!\n Instructions \n Enter Y to continue and Q to quit the game")
play = input("Do you want to play a game?")
if play == "y":
    print("welcome buckle up")


def my_game():

    empty_list = []
    empty_string = ""
    for x in entry:
        if int(x) in new_list:
            print(f"{int(x)} close")
            empty_list.append(int(x))
            empty_string += x
        else:
            pass
    if len(empty_list) == 0:
        print("nope")

    else:
        global c = 0
        for i in empty_list:
            pos_entry = entry.index(str(i))
            pos_empty_list = empty_list.index(i)
            if pos_entry == pos_empty_list:
                print(f" {i} match")
            c += 1

            if c == 3:
                print(f"bravo you guess the secret number {empty_string}")

while True:
    try:
        entry = input("Enter a 3-digit number:")
        my_game()
        if c == 3:
            break

    except ValueError:
        print("only numbers")
