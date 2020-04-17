"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random

off_set = f"\b" * 36

high_score = 999

print(f"""\n\n\t__________________________________________
\t|========================================|
\t|=========>Number Guessing Game<=========|
\t|========================================|""")

def play_again():
    # ask if they want to play again.
    prompt = input(f"""\t|===Would you like to play again?========|
\t|===[y]es, [n]o==========================|
\t|===>   <================================|{off_set}""")
    if prompt.lower() == 'y':
        print(f'''\t|========================================|
        |==============*High Score*==============|
        |=================>*{high_score}*<==================|
        |========================================|''')
        start_game()

    elif prompt.lower() == 'n':
        print(f'''\t|===Thank you for playing.===============|
        |==============*High Score*==============|
        |=================>*{high_score}*<==================|
        |========================================|''')
    else:
        print(f'''\t|===Invalid input.=======================|
        |===Please enter [y] for yes=============|
        |===or [n] for no.=======================|
        |========================================|''')
        play_again()


def print_boxed(text):
    print(f'\t|==={text}')

def start_game():

    num_of_guess = 0

    answer = random.randrange(1,11)

    print(f"\t|===Guess the number between 1 and 10.===|")


    while True:
        global high_score
        # found (global) on stack overflow inorder to bring the variable high_score
        # to the correct scope.
        num_of_guess += 1
        try:
            guess = int(input(f"\t|===>   <================================|{off_set}" ))
                    #needs an off-set of -36 to hit the center of =>  <=
            if guess > 10 or guess < 0:
                print(f'\t|=Please enter a number between 1 and 10=|')
                continue

        except ValueError:
            print_boxed(f'you failed to enter a valid number,==|')
            print_boxed('Please try again.====================|')
            continue



        if guess == answer:
            print(f'''\t|========================================|
        |===Good job! it only took {num_of_guess} trys!=======|''')
            if num_of_guess < high_score:
                high_score = num_of_guess
                print_boxed(f'''Your new high score is {high_score}=============|
        |========================================|''')
            elif num_of_guess >= high_score:
                print(f'''\t|=You did not beat your high score of {high_score}.=|
        |========================================|''')
            break

        elif guess > answer:
            print_boxed("Its lower.===========================|")

        elif guess < answer:
            print_boxed("Its higher.==========================|")




    play_again()
















if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
