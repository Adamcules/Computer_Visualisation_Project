import random

print ("Welcome to the classic game of Rock Paper Scissors. First to win 3 rounds wins the game!")

user_wins = 0
computer_wins = 0

def get_computer_choice():
    # Computer randomly selects option:
    c_choice = random.choice(["Rock", "Paper", "Scissors"])
    return (c_choice)


def get_user_choice():
    # Set 'Rock', 'Paper', 'Scissor' options for user as '1', '2' and '3' within dictionary for speed of entry:
    options = {"1":"Rock", "2":"Paper", "3":"Scissors"}  

    # while loop checks if input is a '1', '2' or '3':
    while True:
        u_choice = input("Enter '1' for 'Rock', '2' for 'Paper' or '3' for 'Scissors':")
        if u_choice in options:
            return options[u_choice]          
        else:
            print ("You must enter either a '1', '2' or '3' as your choice!")


def get_winner (computer_choice, user_choice):
    # Check who has won the round and update number of rounds won by either user or computer:
    global computer_wins
    global user_wins
    if computer_choice == user_choice:
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
        get_winner(get_computer_choice(), get_user_choice())
        print (f"You have won {user_wins} round(s)")
        print (f"Computer has won {computer_wins} round(s)")
    else:
        if user_wins == 3:
            print ("Congratulations, you have reached 3 wins and beaten the computer!")
        elif computer_wins == 3:
            print ("Bad luck, the computer has reached 3 wins and beaten you!")

if __name__ == "__main__":
    play()

