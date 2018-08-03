from time import sleep
import random
def main():
    #Variables representing different positions
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0
    x6 = 0
    x7 = 0
    x8 = 0
    x9 = 0
    x1taken = False
    x2taken = False
    x3taken = False
    x4taken = False
    x5taken = False
    x6taken = False
    x7taken = False
    x8taken = False
    x9taken = False
    user1win = False
    user2win = False
    playerstart = random.randint(1, 2)
    counter = playerstart
    print("Here are the locations of all the positions:")
    sleep(1)
    print("1  2  3")
    sleep(0.5)
    print("4  5  6")
    sleep(0.5)
    print("7  8  9")
    sleep(1)
    print("To choose a position just enter the number.")
    sleep(1)
    print("Designate a player 1 and player 2")
    input("Press enter when ready >")
    print("Flipping the coin...")
    sleep(2)
    print("Player " + str(playerstart) + " begins")
    while ((user1win == False) and (user2win == False )):
        choice = input("Player " + str(counter) + " please choose your position (1-9)")
        if (int(choice) == 1):
            if (x1taken == False):
                x1 = counter
                print(str(x1) + "  " + str(x2) + "  " + str(x3))
                print(str(x4) + "  " + str(x5) + "  " + str(x6))
                print(str(x7) + "  " + str(x8) + "  " + str(x9))
                x1taken = True
                if (counter == 1):
                    counter += 1
                else:
                    counter -= 1
            else:
                print("Stop trying to cheat!")
                if (counter == 1):
                    user2win = True
                else:
                    user1win = True
        elif (int(choice) == 2):
            if (x2taken == False):
                x2 = counter
                print(str(x1) + "  " + str(x2) + "  " + str(x3))
                print(str(x4) + "  " + str(x5) + "  " + str(x6))
                print(str(x7) + "  " + str(x8) + "  " + str(x9))
                x2taken = True
                if (counter == 1):
                    counter += 1
                else:
                    counter -= 1
            else:
                print("Stop trying to cheat!")
                if (counter == 1):
                    user2win = True
                else:
                    user1win = True
                    
        elif (int(choice) == 3):
            if (x3taken == False):    
                x3 = counter
                print(str(x1) + "  " + str(x2) + "  " + str(x3))
                print(str(x4) + "  " + str(x5) + "  " + str(x6))
                print(str(x7) + "  " + str(x8) + "  " + str(x9))
                x3taken = True
                if (counter == 1):
                    counter += 1
                else:
                    counter -= 1
            else:
                print("Stop trying to cheat!")
                if (counter == 1):
                    user2win = True
                else:
                    user1win = True       
                    
        elif (int(choice) == 4):
            if (x4taken == False):  
                x4 = counter
                print(str(x1) + "  " + str(x2) + "  " + str(x3))
                print(str(x4) + "  " + str(x5) + "  " + str(x6))
                print(str(x7) + "  " + str(x8) + "  " + str(x9))
                x4taken = True
                if (counter == 1):
                    counter += 1
                else:
                    counter -= 1
            else:
                print("Stop trying to cheat!")
                if (counter == 1):
                    user2win = True
                else:
                    user1win = True    
                    
        elif (int(choice) == 5):
            if (x5taken == False):    
                x5 = counter
                print(str(x1) + "  " + str(x2) + "  " + str(x3))
                print(str(x4) + "  " + str(x5) + "  " + str(x6))
                print(str(x7) + "  " + str(x8) + "  " + str(x9))
                x5taken = True
                if (counter == 1):
                    counter += 1
                else:
                    counter -= 1
            else:
                print("Stop trying to cheat!")
                if (counter == 1):
                    user2win = True
                else:
                    user1win = True                 
                    
        elif (int(choice) == 6):
            if (x6taken == False):     
                x6 = counter
                print(str(x1) + "  " + str(x2) + "  " + str(x3))
                print(str(x4) + "  " + str(x5) + "  " + str(x6))
                print(str(x7) + "  " + str(x8) + "  " + str(x9))
                x6taken = True
                if (counter == 1):
                    counter += 1
                else:
                    counter -= 1
            else:
                print("Stop trying to cheat!")
                if (counter == 1):
                    user2win = True
                else:
                    user1win = True    
                    
        elif (int(choice) == 7):
            if (x7taken == False):  
                x7 = counter
                print(str(x1) + "  " + str(x2) + "  " + str(x3))
                print(str(x4) + "  " + str(x5) + "  " + str(x6))
                print(str(x7) + "  " + str(x8) + "  " + str(x9))
                x7taken = True
                if (counter == 1):
                    counter += 1
                else:
                    counter -= 1
            else:
                print("Stop trying to cheat!")
                if (counter == 1):
                    user2win = True
                else:
                    user1win = True   
                    
        elif (int(choice) == 8):
            if (x8taken == False):
                x8 = counter
                print(str(x1) + "  " + str(x2) + "  " + str(x3))
                print(str(x4) + "  " + str(x5) + "  " + str(x6))
                print(str(x7) + "  " + str(x8) + "  " + str(x9))
                x8taken = True
                if (counter == 1):
                    counter += 1
                else:
                    counter -= 1
            else:
                print("Stop trying to cheat!")
                if (counter == 1):
                    user2win = True
                else:
                    user1win = True   
                    
        elif (int(choice) == 9):
            if (x9taken == False):    
                x9 = counter
                print(str(x1) + "  " + str(x2) + "  " + str(x3))
                print(str(x4) + "  " + str(x5) + "  " + str(x6))
                print(str(x7) + "  " + str(x8) + "  " + str(x9))
                x9taken = True
                if (counter == 1):
                    counter += 1
                else:
                    counter -= 1
            else:
                print("Stop trying to cheat!")
                if (counter == 1):
                    user2win = True
                else:
                    user1win = True                   
           
    ##Begins check for player 1
           
        #Vertical
        if (x1 == 1) and (x2 == 1) and (x3 == 1):
            user1win = True
            
        elif (x4 == 1) and (x5 == 1) and (x6 == 1):
            user1win = True        
            
        elif (x7 == 1) and (x8 == 1) and (x9 == 1):
            user1win = True   
        
        #Horizontal
        elif (x1 == 1) and (x4 == 1) and (x7 == 1):
            user1win = True        
            
        elif (x2 == 1) and (x5 == 1) and (x8 == 1):
            user1win = True        
            
        elif (x3 == 1) and (x6 == 1) and (x9 == 1):
            user1win = True     
            
        #Diagonal    
        elif (x1 == 1) and (x5 == 1) and (x9 == 1):
            user1win = True    
            
        elif (x3 == 1) and (x5 == 1) and (x7 == 1):
            user1win = True    
            
       
    ##Begins check for player 2
       
        #Vertical
        elif (x1 == 2) and (x2 == 2) and (x3 == 2):
            user2win = True
                
        elif (x4 == 2) and (x5 == 2) and (x6 == 2):
            user2win = True        
                
        elif (x7 == 2) and (x8 == 2) and (x9 == 2):
            user2win = True   
            
        #Horizontal
        elif (x1 == 2) and (x4 == 2) and (x7 == 2):
            user2win = True        
                
        elif (x2 == 2) and (x5 == 2) and (x8 == 2):
            user2win = True        
                
        elif (x3 == 2) and (x6 == 2) and (x9 == 2):
            user2win = True     
                
        #Diagonal    
        elif (x1 == 2) and (x5 == 2) and (x9 == 2):
            user2win = True    
                
        elif (x3 == 2) and (x5 == 2) and (x7 == 2):
            user2win = True  
            
        elif x1taken and x2taken and x3taken and x4taken and x5taken and x6taken and x7taken and x8taken and x9taken:
            break
            
    if (user1win == True):
        print("Congratulations! Player 1 wins!")
        
    elif (user2win == True):
        print("Congratulations! Player 2 wins!")        
    else:
        print("It's a Tie! Please play again!")
       
 
main()