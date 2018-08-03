import time
from random import choice


def main(): #Choices
    playagain = True
    while playagain:
        userchoice = input("Please choose either rock, paper, or scissors >> ").lower()
        choices = ['rock', 'paper', 'scissors']
    
        comp_choice = choice(choices)
        print("The computer chose:", comp_choice)
        
        if userchoice == comp_choice:
            print("DRAW. Please try again.")
        else:
            won = check_win(userchoice, comp_choice)
            if won:
                print("You win!")
            else:
                print("You lost.")
                
        playagain = False
        userplayagain = input("Would you like to play again? Yes/No >> ").lower()

        if userplayagain == "yes":
            playagain = True
        
        else:
            print("Thank you for playing!")
            playagain = False

    
def check_win(userchoice, comp_choice): #Checks if user wins or loses
    rock     = (userchoice == "rock") and (comp_choice == "scissors")
    paper    = (userchoice == "paper") and (comp_choice == "rock")
    scissors = (userchoice == "scissors") and (comp_choice == "paper")
    
    return rock or paper or scissors

main()