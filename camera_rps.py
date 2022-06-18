import random
import time
import numpy as np
import modified_model_download_code

print ("Welcome to Rock Paper Scissors. First to win 3 rounds wins the game!")

user_wins = 0
computer_wins = 0

def get_computer_choice():
    # Computer randomly selects option:
    c_choice = random.choice(["Rock", "Paper", "Scissors"])
    return (c_choice)


def get_prediction():
    modified_model_download_code.run_model()
    p_list = modified_model_download_code.prediction[0]
    max_value = max(p_list)
    ind_value = (np.where(p_list == max_value))[0]
    if ind_value == 0:
        return "Nothing"
    elif ind_value == 1:
        return "Rock"
    elif ind_value == 2:
        return "Paper"
    elif ind_value == 3:
        return "Scissors"


def get_winner (computer_choice, user_choice):
    # Check who has won the round and update number of rounds won by either user or computer:
    global computer_wins
    global user_wins
    if user_choice == "Nothing":
        print ("Please signal whether you choose 'Rock', 'Paper' or 'Scissors'")
    elif computer_choice == user_choice:
        print (f"Round is tied: '{computer_choice}' ties '{user_choice}'")
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            print (f"You win!: 'Paper' beats 'Rock'")
            user_wins += 1 
        elif user_choice == "Scissors":
            print (f"You lose!: 'Scissors' loses to 'Rock'")
            computer_wins += 1 
    elif computer_choice == "Paper":
        if user_choice == "Rock":
            print (f"You lose!: 'Rock' loses to 'Paper'")
            computer_wins += 1
        elif user_choice == "Scissors":
            print (f"You win!: 'Scissors' beats 'Paper'")
            user_wins += 1
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            print (f"You win!: 'Rock' beats 'Scissors'")
            user_wins += 1
        elif user_choice == "Paper":
            print (f"You lose!: 'Paper' loses to 'Scissors'")
            computer_wins += 1

def play(): 
    while user_wins < 3 and computer_wins < 3:
        computer_choice = get_computer_choice()
        user_choice = get_prediction()
        get_winner(computer_choice, user_choice)
        print (f"You have won {user_wins} round(s)")
        print (f"Computer has won {computer_wins} round(s)")
        if user_wins < 3 and computer_wins < 3: 
            start_round = input("Press 'Enter' key to start next round")
    else:
        if user_wins == 3:
            print ("Congratulations, you have reached 3 wins and beaten the computer!")
        elif computer_wins == 3:
            print ("Bad luck, the computer has reached 3 wins and beaten you!")

if __name__ == "__main__":
    play()

