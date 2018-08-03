import time
import random
def main():
    usrInp = input("Please guess a number within 1-20")

    number = str(random.randint(1,20))
    if usrInp == number:
        print("I guessed the same! Congrats!")
    else:
            print("Not this time! Sorry.")

main()