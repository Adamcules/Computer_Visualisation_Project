# Computer_Visualisation_Project

This project was to create a traditional 'Rock', 'Paper', 'Scissors' game played against the computer. First with a manual input for the user and then with a camera controlled input from the user.

Created new environment for the game, downloading the following: opencv-python, tensorflow, and ipykernel.

Created the manual game using 4 functions. A function for the computer input (get_computer_choice), a function for the user input (get_user_choice), a function that determines whether the computer or user won a round (get_winner) and a function for initiating the game and determining the end condition for the whole game i.e. when either the computer or user reaches 3 round wins (play).

The get_computer_choice function uses the 'random.choice' function to retrun a random choice for the computer. 
The get_user_choice function sets up a dictionary for the user input options (i.e. 1 : Rock, 2 : Paper, 3 : Scissors) and then required the user to input a 1, 2 or 3 as their choice. This was done in order to make user input entry much quicker. It also makes use of a while loop to check whether the user has correctly entered a 1, 2 or 3.
The get_winner function uses a series if/elif statements to determine whether the computer or user won a round.
The play function is called to initiate the game and makes use of a while loop to continue the game until either the computer or user has reached 3 round wins, thus determining the end of the game. 

