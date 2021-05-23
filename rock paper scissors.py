import random

comp_wins = 0
player_wins = 0

#User Input
def choose_option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R","ROCK"]:
        user_choice = "r"
    elif user_choice in ["paper", "Paper", "p", "P","PAPER"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "sc", "SC","SCISSORS"]:
        user_choice = "sc"
    else:
        print("Input Unknown, I Don't Understand")
        choose_option()
    return user_choice

def computer_option():
    comp_choice = random.randint(1, 3) #Outputs 1, 2, or 3
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    elif comp_choice == 3:
        comp_choice = "sc"
    return comp_choice


#=============================================================================
#MAIN
while True:
    print("")

    user_choice = choose_option()
    comp_choice = computer_option()

    print("")

    #If the User Chooses Rock
    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock. The computer chose rock. You Tied.")

        elif comp_choice == "p":
            print("You chose rock. The computer chose paper. You Lose.")
            comp_wins += 1

        elif comp_choice == "sc":
            print("You chose rock. The computer chose scissors. You Win.")
            player_wins += 1

    # If the User Chooses Paper
    if user_choice == "p":
        if comp_choice == "r":
            print("You chose paper. The computer chose rock. You Win.")
            player_wins += 1

        elif comp_choice == "p":
            print("You chose paper. The computer chose paper. You Tie.")

        elif comp_choice == "sc":
            print("You chose paper. The computer chose scissors. You Lose.")
            comp_wins += 1

    # If the User Chooses Scissors
    if user_choice == "sc":
        if comp_choice == "r":
            print("You chose scissors. The computer chose rock. You Lose.")
            comp_wins += 1

        elif comp_choice == "p":
            print("You chose scissors. The computer chose paper. You Win.")
            player_wins += 1

        elif comp_choice == "sc":
            print("You chose scissors. The computer chose scissors. You Tie.")

    print("")
    print("The Number of Player Wins:" + str(player_wins))
    print("The Number of Computer Wins:" + str(comp_wins))
    print("")

    #Ask if the Player Wants to Play Again?
    choice = input("Do You Want to Play Again? (Y/N)")
    if choice in ["Y", "y", "Yes", "yes","YES"]:
        pass
    elif choice in ["N", "n", "No", "no", "NO"]:
        break
    else:
        break