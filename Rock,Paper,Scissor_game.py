import random

user_wins =0
computer_wins = 0

actions=['rock', 'paper', 'scissors']

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    if user_input not in actions :
        continue
    random_number = random.randint(0,2)
    computer_pick = actions[random_number]
    print("Computer Picks",computer_pick + ".")

    if user_input == "rock" and computer_pick =="scissors" :
        print("You won :)")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock" :
        print("You won :)")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper" :
        print("You won :)")
        user_wins += 1
    else:
        print("You lost :(")
        computer_wins +=1


print("You Won", user_wins,"times :)")
print("The Computer Won",computer_wins,"times.")
print("GoodBye!")
    
