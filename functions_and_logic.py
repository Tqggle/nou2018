def main():
    gender = input("Welcome to choose your own path! To begin, are you a Male or a Female (m/f)")
    if (gender == "m" or gender == "f"):
        if gender == "m":
            malestory()
        elif gender == "f":
            femalestory()
    else: 
        print("Invalid Selection")
def malestory():
    ##BEGINS THE MALE STORY
    print("The guy walked to the candy store")
    fruit = input("Hello Male! Welcome to Fruit Fun! Choose: Would you like to purchase a nice, shiny red apple (a), or a off-ish looking orange (o)? Please return with a for apple, or o for orange.")
    if (fruit == "a" or fruit == "o"):
        if fruit == "a":
            apple()
        elif fruit == "o":
            orange()
        else:
            print("Invalid Selection")
            
def apple():
    #Code for choosing apple in selection 2
    print("Nice choice! You survived. Beginning stage 2")
    
def orange():
    #Code for choosing orange in selection 2
    print("GAME OVER! Please play again.")
   
def femalestory():
    ##BEGINS THE FEMALE STORY
    print("The girl walked to the candy store")
    fruit = input(" Hello Female! Welcome to Fruit Fun! Choose: Would you like to purchase a nice, shiny red apple (a), or a off-ish looking orange (o)? Please return with (a) for apple, or (o) for orange.")
    if (fruit == "a" or fruit == "o"):
        if fruit == "a":
            apple()
        elif fruit == "o":
            orange()
        else:
            print("Invalid Selection")
            
def apple():
    #Code for choosing apple in selection 2
    print("Nice choice! You survived. Beginning stage 2.")    
        
def orange():
    #Code for choosing orange in selection 2
    print("GAME OVER! Please play again.")        
        
    
    
main ()