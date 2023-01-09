import random 
  
rock= 1 
paper= 2 
scissors= 3 
  
print ("input 1 if you want to use rock") 
print ("input 2 if you want to use paper") 
print ("input 3 if you want to use scissors") 
print("") 
computer = random.randint(1,3) 
User_Choice = int(input("please pick rock,paper or scissors")) 
  
if User_Choice == computer: 
    print("Draw!") 
     
if User_Choice   == 1: 
    if computer == 2: 
        print("computer! wins as paper wraps rock.") 
    if computer == 3: 
        print("You win! as rock blunts scissors") 
         
if User_Choice == 2: 
    if computer == 1: 
        print("You win as paper wraps rock") 
    if computer == 3: 
        print("computer wins! as scissors cuts paper") 
         
if User_Choice == 3: 
    if computer == 2: 
        print("You win! scissors cuts paper ") 
    if computer == 1: 
        print("computer wins! as rock blunt scissors") 

