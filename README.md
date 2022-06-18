# Computer_Visualisation_Project

Aim of project was to create a traditional 'Rock', 'Paper', 'Scissors' game played against the computer. First with a manual input for the user (manual_rps.py) and then with a camera controlled input from the user (camera_rps.py).

Created new environment for the game, downloading the following: opencv-python, tensorflow, and ipykernel.

First created the manual game using 4 functions. A function for the computer input (get_computer_choice), a function for the user input (get_user_choice), a function that determines whether the computer or user won a round (get_winner) and a function for initiating the game and determining the end condition for the whole game i.e. when either the computer or user reaches 3 round wins (play).

The get_computer_choice function uses the 'random.choice' function to retrun a random choice for the computer. 
The get_user_choice function sets up a dictionary for the user input options (i.e. 1 : Rock, 2 : Paper, 3 : Scissors) and then required the user to input a 1, 2 or 3 as their choice. This was done in order to make user input entry much quicker. It also makes use of a while loop to check whether the user has correctly entered a 1, 2 or 3.
The get_winner function uses a series if/elif statements to determine whether the computer or user won a round.
The play function is called to initiate the game and makes use of a while loop to continue the game until either the computer or user has reached 3 round wins, thus determining the end of the game.


For the camera controlled version of the game, a model was created using the machine learning tool on website 'Teachable Machine'. Four classes were created within the model: 'Nothing', 'Rock', 'Paper' and 'Scissors'. The model file was called keras_model.h5 and downloaded.
Code was downloaded from the AI-Core teaching programme to run the keras model which opens the local camera and then outputs a prediction of which class is being viewed as a numpy array.

The code for the camera controlled game was nearly identical to the manual game except that the get_user_choice function was replaced with the get_prediction function. This new function made calls to the 'prediction' variable from the imported modified_model_download_code.py file. This file was modified from the original AI-Core file to introduce a 5 second timer to close the camera window using the time.time() function, and a new function called camera_loop and run_model were defined in order that calls could be made from the main file to run the code properly within this imported module. 
A user input was added to the 'play' function such that a user has to press enter in between rounds to start the next round.







