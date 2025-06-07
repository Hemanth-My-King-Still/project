import random  
play = ["Rock", "Paper", "Scissors"] 
computer = play[random.randint(0,2)] 
you = False
while you == False:  
    you = input("Rock, Paper, Scissors?") 
    if you == computer: 
        print("Tie!") 
    elif you == "Rock": 
        if computer == "Paper": 
            print("You lose!", computer, "covered", you) 
        else: 
            print("You win!", you, "smashed", computer) 
    elif you == "Paper": 
        if computer == "Scissors": 
            print("You lose!", computer, "cuts", you) 
        else: 
            print("You win!", you, "covered", computer) 
    elif you == "Scissors": 
        if computer == "Rock": 
            print("You lose!", computer, "smashed", you) 
        else: 
            print("You win!", you, "cuts", computer) 
    else: 
        print("That's not a valid play. Give the coorect spelling!") 

    you = False 
    computer = play[random.randint(0,2)]

    
