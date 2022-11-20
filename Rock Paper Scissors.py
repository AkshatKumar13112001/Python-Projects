import random

user_wins = 0
computer_wins = 0
ties = 0

options = ["Rock","Paper","Scissors"]

while True:
    user_input = input("Rock/Paper/Scissors or Quit:")
    if user_input == "Quit":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)

    computer_pick = options [random_number]

    print("Computer picked", computer_pick + ".")

    if user_input == "Rock" and computer_pick == "Scissor":
        print ("Win")
        user_wins += 1

    elif user_input == "Paper" and computer_pick == "Rock":
        print ("Win")
        user_wins += 1

    elif user_input == "Scissors" and computer_pick == "Paper":
        print ("Win")
        user_wins += 1

    elif user_input == computer_pick:
        print ("Tie")
        ties += 1

    else:
        print ("Loss")
        computer_wins +=1

print ( "Result", user_wins, "Wins", computer_wins, "Losses", ties, "Ties")
