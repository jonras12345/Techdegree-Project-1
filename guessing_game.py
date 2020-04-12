"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

off_set = f"\b" * 36

high_score = 999

print(f"""\n\n\t__________________________________________
\t|========================================|
\t|=========>Number Guessing Game<=========|
\t|========================================|""")


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    num_of_guess = 0



    answer = random.randrange(1,11)
    print(f"\t|===Guess the number between 1 and 10.===|")


    while True:
        global high_score
        num_of_guess += 1

        guess = int(input(f"\t|===>   <================================|{off_set}" ))
                        #needs an off-set of -36 to hit the center of =>  <=


        if guess == answer:
            print(f'\t|===Good job! it only took {num_of_guess} trys!=======|')
            if num_of_guess < high_score:
                high_score = num_of_guess
                print(f'\t|===Your new high score is {high_score}=============|')
            elif num_of_guess >= high_score:
                print(f'''\t|=You did not beat your high score of {high_score}.=|
        |===please try again.====================|''')
            break

        elif guess > answer:
            print(f"\t|===Its lower.===========================|")

        elif guess < answer:
            print(f"\t|===Its higher.==========================|")

    prompt = input(f"""\t|===Would you like to play again?========|
    \t|===[y]es, [n]o==========================|
    \t|===>   <================================|{off_set}""")
    if prompt == 'y':
        start_game()

    else:
        print(f"\t|===Thank you for playing.===============|")
















if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
