import random
min = 1
max = 6

def main():
    roll_again = "y"
    while role_again == "yes" or roll_again == "y":
        rollbegin = input('Press \"ENTER\" to roll the dice!')
        print("You rolled a", random.randint(min,max))
        roll_again = input("Would you like to roll the dice again? y/n")


main()