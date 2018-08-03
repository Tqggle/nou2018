from random import choice

def main(): #Nickname Generator Begins Here
    
    input("To generate a random nickname click any key on the keyboard! >> ").lower()
    
    
    name1 = ['Giant', 'Miniature']
    
    random1 = choice(name1)
    
    name2 = ['Smelly', 'Unicorn']
    
    random2 = choice(name2)
    
    name3 = ['Monster', 'Beast']
    
    random3 = choice(name3)
    
    print('Your nickname is: ' random1 + random2 + random3)
    
    
    
main()