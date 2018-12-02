# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the number of feet corresponding to a number of miles.

###################################################
# Miles to feet conversion formula
# Student should enter function on the next lines.

def miles_to_feet(miles):
    return 5280 * miles

###################################################
# Tests
# Student should not change this code.

print('Problem 1:\n')
def test_1(miles):
    print (str(miles) + " miles equals,")
    print (str(miles_to_feet(miles)) + " feet.\n")
    

test_1(13)
test_1(57)
test_1(82.67)
print ('--------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#13 miles equals 68640 feet.
#57 miles equals 300960 feet.
#82.67 miles equals 436497.6 feet.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the number of seconds in a given number of hours, minutes, and seconds.

###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter function on the next lines.
def total_seconds(hours, minutes, seconds):
    """Returns the number of seconds in the given number of hours, minutes, and seconds."""
    
    return (hours * 60 + minutes) * 60 + seconds


###################################################
# Tests
# Student should not change this code.
print('Problem 2:\n')

def test_2(hours, minutes, seconds):
    """Tests the total_seconds functions."""
    
    print (str(hours) + " hours, " + str(minutes) + " minutes, and,")
    print (str(seconds) + " seconds totals to,")
    print (str(total_seconds(hours, minutes, seconds)) + " seconds.\n")

test_2(7, 21, 37)
test_2(10, 1, 7)
test_2(1, 0, 1)

print ('--------------------------------------\n')


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.
#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.
#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the length of a rectangle's perimeter, given its width and height.

###################################################
# Rectangle perimeter formula
# Student should enter function on the next lines.

def rectangle_perimeter(width, height):
    return 2 * width + 2 * height

###################################################
# Tests
# Student should not change this code.

print('Problem 3:\n')

def test_3(width, height):
    print ("A rectangle " + str(width) + " inches wide and " + str(height)+ ',')
    print ("inches high has a perimeter of,")
    print (str(rectangle_perimeter(width, height)) + " inches.\n")

test_3(4, 7)
test_3(7, 4)
test_3(10, 10)
print ('--------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.
#A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.
#A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the area of a rectangle, given its width and height.

###################################################
# Rectangle area formula
# Student should enter function on the next lines.

def rectangle_area(width, height):
    return width * height


###################################################
# Tests
# Student should not change this code.

print('Problem 4:\n')

def test_4(width, height):
    """Tests the rectangle_area function."""
    
    print ("A rectangle " + str(width) + " inches wide and " + str(height)+',')
    print ("inches high has an area of,")
    print (str(rectangle_area(width, height)) + " square inches.\n")

test_4(4, 7)
test_4(7, 4)
test_4(10, 10)

print ('--------------------------------------\n')
    
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.
#A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.
#A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the circumference of a circle, given the length of its radius.

###################################################
# Circle circumference formula
# Student should enter function on the next lines.

def circle_circumference(radius):
    PI = 3.14
    return 2*PI*radius

###################################################
# Tests
# Student should not change this code.

print('Problem 5:\n')

def test_5(radius):
    print ("A circle with a radius of " + str(radius)+',')
    print ("inches has a circumference of,")
    print (str(circle_circumference(radius)) + " inches.\n")

test_5(8)
test_5(3)
test_5(12.9)

print ('--------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A circle with a radius of 8 inches has a circumference of 50.2654824574 inches.
#A circle with a radius of 3 inches has a circumference of 18.8495559215 inches.
#A circle with a radius of 12.9 inches has a circumference of 81.0530904626 inches.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the area of a circle, given the length of its radius.

###################################################
# Circle area formula
# Student should enter function on the next lines.

def circle_area(radius):
    PI = 3.14
    return PI*radius**2

###################################################
# Tests
# Student should not change this code.

print('Problem 6:\n')

def test_6(radius):
    print ("A circle with a radius of " + str(radius)+',')
    print ("inches has an area of,")
    print (str(circle_area(radius)) + " square inches.\n")

test_6(8)
test_6(3)
test_6(12.9)

print ('--------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A circle with a radius of 8 inches has an area of 201.06192983 square inches.
#A circle with a radius of 3 inches has an area of 28.2743338823 square inches.
#A circle with a radius of 12.9 inches has an area of 522.792433484 square inches.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the future value of a given present value, annual rate, and number of years.

###################################################
# Future value formula
# Student should enter function on the next lines.

def future_value(present_value, annual_rate, years):
    return present_value * (  (1 + (0.01 * annual_rate)) ** years)

###################################################
# Tests
# Student should not change this code.

print('Problem 7:\n')

def test_7(present_value, annual_rate, years):
    """Tests the future_value function."""
    
    print ("The future value of $" + str(present_value) + " in " + str(years)+',')
    print ("years at an annual rate of " + str(annual_rate) + "% is,")
    print ("$" + str(future_value(present_value, annual_rate, years)) + ".\n")


###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

test_7(1000, 7, 10)
test_7(200, 4, 5)
test_7(1000, 3, 20)

print ('--------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.
#The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.
#The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute a name tag, given the first and last name.

###################################################
# Name tag formula
# Student should enter function on the next lines.

def name_tag(first_name, last_name):
    return 'My name is ' + str(first_name) + str(last_name) + '.'

###################################################
# Tests
# Student should not change this code.

print('Problem 8:\n')

def test_8(first_name, last_name):
    print (name_tag(first_name, last_name))
    
test_8("Joe", "Warren")
test_8("Scott", "Rixner")
test_8("John", "Greiner")

print ('--------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#My name is Joe Warren.
#My name is Scott Rixner.
#My name is John Greiner.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the statement about a person's name and age, given the person's name and age.

###################################################
# Name and age formula
# Student should enter function on the next lines.

def name_and_age(name, age):
    return str(name) + ' is ' + str(age) + ' years old.'

###################################################
# Tests
# Student should not change this code.

print('Problem 9:\n')
      
def test_9(name, age):
    print (name_and_age(name, age))
    
test_9("Joe Warren", 52)
test_9("Scott Rixner", 40)
test_9("John Greiner", 46)

print ('--------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe Warren is 52 years old.
#Scott Rixner is 40 years old.
#John Greiner is 46 years old.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the distance between the points (x0, y0) and (x1, y1).

###################################################
# Distance formula
# Student should enter function on the next lines.

# Hint: You need to use the power operation ** .

def point_distance(x0, y0, x1, y1):
    return ( (( x0 - x1) ** 2) + (( y0 - y1) ** 2) ) ** 0.5
    
###################################################
# Tests
# Student should not change this code.

print('Problem 10:\n')

def test_10(x0, y0, x1, y1):
    print ("The distance from (" + str(x0) + ", " + str(y0) + ") to,")
    print ("(" + str(x1) + ", " + str(y1) + ") is,")
    print (str(point_distance(x0, y0, x1, y1)) + ".\n")

test_10(2, 2, 5, 6)
test_10(1, 1, 2, 2)
test_10(0, 0, 3, 4)

print ('--------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The distance from (2, 2) to (5, 6) is 5.0.
#The distance from (1, 1) to (2, 2) is 1.41421356237.
#The distance from (0, 0) to (3, 4) is 5.0.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the area of a triangle (using Heron's formula),
# given its side lengths.

###################################################
# Triangle area (Heron's) formula
# Student should enter function on the next lines.
# Hint:  Also define point_distance as use it as a helper function.

def triangle_area(x0, y0, x1, y1, x2, y2):
    a = ((( x0 - x1) ** 2) + (( y0 - y1) ** 2)) ** 0.5
    b = ((( x1 - x2) ** 2) + (( y1 - y2) ** 2)) ** 0.5
    c = ((( x0 - x2) ** 2) + (( y0 - y2) ** 2)) ** 0.5

    s = 0.5 * ( a + b + c)
    
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

###################################################
# Tests
# Student should not change this code.

print('Problem 11:\n')

def test_11(x0, y0, x1, y1, x2, y2):
    print ("A triangle with vertices (" + str(x0) + "," + str(y0) + "),")
    print ("(" + str(x1) + "," + str(y1) + "), and," +
     "(" + str(x2) + "," + str(y2) + ") has an area of,")
    print (str(triangle_area(x0, y0, x1, y1, x2, y2)) + ".\n")

test_11(0, 0, 3, 4, 1, 1)
test_11(-2, 4, 1, 6, 2, 1)
test_11(10, 0, 0, 0, 0, 10)

print ('--------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute and print tens and ones digit of an integer in [0,100).

###################################################
# Digits function
# Student should enter function on the next lines.

def print_digits(num):
    print('The tens digit is {}, and the ones digit is {}'
          '.\n'.format(num//10,num%10))
    
###################################################
# Tests
# Student should not change this code.

print('Problem 12:\n')

print_digits(42)
print_digits(99)
print_digits(5)

print ('--------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.
import random 

def powerball():
    list_num = [random.randrange(1, 60) for i in range(5)]
    powerball = random.randrange(1, 36)
    
    print('Today’s numbers are {}, {}, {}, {}, and {}.'
          'The Powerball numberis {}'
          '.'.format(list_num[0],list_num[1],list_num[2],list_num[3],list_num[4],powerball))
    
###################################################
# Tests
# Student should not change this code.

print('Problem 13:\n')

powerball()
powerball()
powerball()

print ('--------------------------------------\n')