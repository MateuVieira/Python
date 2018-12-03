# Add "Hello" and "Goodbye" buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 


# Handlers for buttons

def print_hello():
    print('Hello')

def print_goodbye():
    print('Goodbye')
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Hello and Goodbye", 200, 200)
frame.add_button("Hello", print_hello)
frame.add_button("Goodbye", print_goodbye)


# Start the frame animation
frame.start()


###################################################
# Test

print('Program 1:\n')

print_hello()
print_hello()
print_goodbye()
print_hello()
print_goodbye()


print('\n ----------------------------------------------\n')
###################################################
# Expected output from test

#Hello
#Hello
#Goodbye
#Hello
#Goodbye
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Register three buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 


# Handlers for buttons
def set_red():
    global color
    color = ("red")
    
def set_blue():
    global color
    color = ("blue")
    
def print_color():
    print (color)

# Create frame
frame = simplegui.create_frame("Set and print colors", 200, 200)
frame.add_button("red", set_red)
frame.add_button("blue", set_blue)
frame.add_button("Print", print_color)
# Start the frame animation
frame.start()


###################################################
# Test

print('Program 2:\n')

set_red()
print_color()
set_blue()
print_color()
set_red()
set_blue()
print_color()

print('\n ----------------------------------------------\n')
###################################################
# Expected output from test

#red
#blue
#blue

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# GUI with buttons to manipulate global variable count

###################################################
# Student should enter their code below


import simplegui

# Define event handlers for four buttons

def reset():
    global count
    count = 0
    
def increment():
    global count
    count += 1
    
def print_count():
    global count
    print (count)
    
def decrement():
    global count
    count -= 1
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Program 3: Count", 200, 200)
frame.add_button("reset", reset)
frame.add_button("increment", increment)
frame.add_button("decrement", decrement)
frame.add_button("print_count", print_count)

# Start the frame animation
frame.start()


    
###################################################
# Test

# Note that the GLOBAL count is defined inside a function

print('Program 3:\n')

reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

print('\n ----------------------------------------------\n')
####################################################
# Expected output from test

#1
#2
#-2

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Echo an input field

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Handlers for input field

def get_input(string):
    print(string)
    
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Echo input", 200, 200)
frame.add_input("Echo input (hit enter)", get_input, 200)

# Start the frame animation
frame.start()


###################################################
# Test
print('Program 4:\n')

get_input("First test input")
get_input("Second test input")
get_input("Third test input")

print('\n ----------------------------------------------\n')
###################################################
# Expected output from test

#First test input
#Second test input
#Third test input

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Convert input text into Pig Latin

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Pig Latin helper function
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.
    if (first_letter == "a" or first_letter == "e" or first_letter == "i" or
        first_letter == "o" or first_letter == "u"):
        return word + "way"
    else:
        return rest_of_word + first_letter + "ay"


# Handler for input field
def get_input(txt):
    print (pig_latin(txt))
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)
frame.add_input("Translate to Pig Latin (hit enter)", get_input, 200)


# Start the frame animation
frame.start()


###################################################
# Test

print('Program 5:\n')

get_input("pig")
get_input("owl")
get_input("tree")

print('\n ----------------------------------------------\n')
###################################################
# Expected output from test

#igpay
#owlway
#reetay

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Insert your solution for RPSLS here

def name_to_number(name):
    """
    delete the following pass statement and fill in your code belo
    convert name to number using if/elif/else
    don't forget to return the result!
    """
    if name == 'rock':
        return 0
    if name == 'Spock':
        return 1
    if name == 'paper':
        return 2
    if name == 'lizard':
        return 3
    if name == 'scissors':
        return 4
    
    print('Error: function - name_to_number -> input out range!!')

def number_to_name(number):
    """
    delete the following pass statement and fill in your code below 
    convert number to a name using if/elif/else
    don't forget to return the result!
    """
    
    if number == 0:
        return 'rock'
    if number == 1:
        return 'Spock'
    if number == 2:
        return 'paper'
    if number == 3:
        return 'lizard'
    if number == 4:
        return 'scissors'
    
    print('Error: function - number_to_name -> input out range!!')

def rpsls(player_choice): 
    """
    delete the following pass statement and fill in your code below
    pass
    print a blank line to separate consecutive games
    print out the message for the player's choice
    convert the player's choice to player_number using the function name_to_number()
    compute random guess for comp_number using random.randrange()
    convert comp_number to comp_choice using the function number_to_name()
    print out the message for computer's choice
    compute difference of comp_number and player_number modulo five
    use if/elif/else to determine winner, print winner message
    """
    import random
    
    print('Player chooses ' + player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    print('Computer chooses ' + comp_choice)
    
    result = (comp_number - player_number) % 5
    
    #print(result)
    if result == 0:
        print('Player and computer tie!\n')
    elif result < 3:
        print('Computer wins!\n')
    else:
        print('Player wins!\n')

     
    
# handler for input field
def get_guess(guess):
    
    # validate input
    if not (guess == "rock" or guess == "Spock" or guess == "paper" or
            guess == "lizard" or guess == "scissors"):
        print
        print ('Error: Bad input "' + guess + '" to rpsls.\n')
        return
    else:
        rpsls(guess)
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#


# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------


