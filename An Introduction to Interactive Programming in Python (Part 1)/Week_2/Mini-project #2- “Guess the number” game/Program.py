# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game
def new_game_100():
    # initialize global variables used in your code here

    global number, tries
    
    print('Start the game: \n --> Game: Range is [0:100)')
    range100()
         
def new_game_1000():
    # initialize global variables used in your code here

    global number, tries
    
    print('Start the game: \n--> Game: Range is [0:1000)')
    range1000()


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    global number, tries
    number = random.randrange(100)
    tries = 7
    print('number of the tries - 7\n')
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global number, tries
    number = random.randrange(1000)
    tries = 10
    print('number of the tries - 10\n')

def reset():
    print('\n --------------------------------- '
          '\n -------End of the Game-----------\n')
    new_game_100()
    
    
def input_guess(guess):
    # main game logic goes here	
    
    global number, tries
    
    if int(guess) == number:
        print('CORRECT!!  number = ' + str(number))
        new_game()
        
    elif int(guess) > number:
        tries -= 1
        if tries == 0:
            reset()
        else:    
            print('Wrong!! Lower, remaining tries: ' + str(tries))
    else:
        tries -= 1
        if tries == 0:
            reset()
        else:    
            print('Wrong!! Higher, remaining tries: ' + str(tries))

    
# create frame
frame = simplegui.create_frame("Guess the number!!", 200, 200)
frame.add_button("Range is [0:100)", new_game_100)
frame.add_button("range is [0:1000)", new_game_1000)
frame.add_label('---------------------------')
frame.add_input("Enter with you guess:", input_guess, 200)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game_100()


# always remember to check your completed program against the grading rubric
