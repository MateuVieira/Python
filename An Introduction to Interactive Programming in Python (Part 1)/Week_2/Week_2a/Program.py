# Printing "Goodbye" with a local message variable

###################################################
# Student should enter function on the next lines.

def print_goodbye():
    message = 'Goodbye'
    print(message)

###################################################
# Tests

print('Program 1:\n')

message = "Hello"
print (message)
print_goodbye()
print (message)

message = "Ciao"
print (message)
print_goodbye()
print (message)

print('\n------------------------------------------\n')

###################################################
# Output

#Hello
#Goodbye
#Hello
#Ciao
#Goodbye
#Ciao
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Printing "Goodbye" with a global message variable

###################################################
# Student should enter function on the next lines.



def print_goodbye():
    global message 
    message = 'Goodbye'
    print(message)

###################################################
# Tests

print('Program 2:\n')

message = "Hello"
print (message)
print_goodbye()
print (message)

message = "Ciao"
print (message)
print_goodbye()
print (message)

print('\n------------------------------------------\n')

###################################################
# Output

#Hello
#Goodbye
#Goodbye
#Ciao
#Goodbye
#Goodbye
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Functions to manipulate global variable count

###################################################
# Student should enter function on the next lines.
# Reset global count to zero.

def reset():
    global count
    count = 0
    
# Increment global count.

def increment():
    global count
    count += 1
    
# Decrement global count.

def decrement():
    global count 
    count -= 1
    
# Print global count.

def print_count():
    #global count
    print(count)
    
###################################################
# Test

# note that the GLOBAL count is defined inside a function

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

print('\n------------------------------------------\n')

####################################################
# Output
#1
#2
#-2
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Open a frame

###################################################
# Open frame
# Student should add code where relevant to the following.

print('Program 4:\n')

import simplegui

message = "My first frame!"

# Handler for mouse click
def click():
    global message
    message = "My first frame!"
    print (message)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("My first frame", 100, 200)
frame.add_button("Click me", click)



# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Open a frame

###################################################
# Open frame
# Student should add code where relevant to the following.

import simplegui 

message = "My second frame!"

# Handler for mouse click
def click():
    message = "My second frame!"
    print (message)

# Assign callbacks to event handlers
frame = simplegui.create_frame("My second frame!", 200, 100)
frame.add_button("Click me", click)

# Start the frame animation
frame.start()

