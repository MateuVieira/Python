# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute whether an integer is even.

###################################################
# Is even formula
# Student should enter function on the next lines.

def is_even(num):
    return True if num % 2 == 0 else False

###################################################
# Tests
# Student should not change this code.

print('Program 1:\n')

def test_1(number):
    """Tests the is_even function."""
    if is_even(number):
        print (number, "is even.\n")
    else:
        print (number, "is odd.\n")

test_1(8)
test_1(3)
test_1(12)

print('---------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#8 is even.
#3 is odd.
#12 is even.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute whether a person is cool.

###################################################
# Is cool formula
# Student should enter function on the next lines.

def is_cool(name):
    return (True if (name == "Joe") or 
                    (name == "John") or
                    (name == "Stephen") 
                 else False)

###################################################
# Tests
# Student should not change this code.

print('Program 2:\n')

def test_2(name):
    """Tests the is_cool function."""
    
    if is_cool(name):
        print (name, "is cool.\n")
    else:
        print (name, "is not cool.\n")

test_2("Joe")
test_2("John")
test_2("Stephen")
test_2("Scott")

print('---------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe is cool.
#John is cool.
#Stephen is cool.
#Scott is not cool.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute whether the given time is lunchtime.

###################################################
# Is lunchtime formula
# Student should enter function on the next lines.

def is_lunchtime(hour, is_am):
    return (True if ( 11 == hour and is_am) or
                    ( 12 == hour and not is_am)
                 else False)

###################################################
# Tests
# Student should not change this code.

print('Program 3:\n')

def test_3(hour, is_am):
    """Tests the is_lunchtime function."""
    print (str(hour) +',')
    if is_am:
        print ("AM,")
    else:
        print ("PM,")
    if is_lunchtime(hour, is_am):
        print ("is lunchtime.\n")
    else:
        print ("is not lunchtime.\n")

test_3(11, True)
test_3(12, True)
test_3(11, False)
test_3(12, False)
test_3(10, False)

print('---------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#11 AM is lunchtime.
#12 AM is not lunchtime.
#11 PM is not lunchtime.
#12 PM is lunchtime.
#10 PM is not lunchtime.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute whether the given year is a leap year.

###################################################
# Is leapyear formula
# Student should enter function on the next lines.
def is_leap_year(year):
    """
    Returns whether the given Gregorian year is a leap year.
    """	
    return ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0))


###################################################
# Tests
# Student should not change this code.

print('Program 4:\n')

def test_4(year):
    """Tests the is_leapyear function."""
    if is_leap_year(year):
        print (year, " is a leap year.\n")
    else:
        print (year, " is not a leap year.\n")

test_4(2000)
test_4(1996)
test_4(1800)
test_4(2013)

print('---------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute whether two intervals intersect.

###################################################
# Interval intersection formula
# Student should enter function on the next lines.

def interval_intersect(a, b, c, d):
    return (c <= b) and (a <= d)

###################################################
# Tests
# Student should not change this code.

print('Program 5:\n')

def test_5(a, b, c, d):
    """Tests the interval_intersect function."""
    print ("Intervals [" + str(a) + ", " + str(b) + "] and [" + str(c) + ", " + str(d) + "],")
    if interval_intersect(a, b, c, d):
        print ("intersect.\n")
    else:
        print ("do not intersect.\n")

test_5(0, 1, 1, 2)
test_5(1, 2, 0, 1)
test_5(0, 1, 2, 3)
test_5(2, 3, 0, 1)
test_5(0, 3, 1, 2)

print('---------------------------------------------\n')


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Intervals [0, 1] and [1, 2] intersect.
#Intervals [1, 2] and [0, 1] intersect.
#Intervals [0, 1] and [2, 3] do not intersect.
#Intervals [2, 3] and [0, 1] do not intersect.
#Intervals [0, 3] and [1, 2] intersect.
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the statement about a person's name and age, given the person's name and age.

###################################################
# Name and age formula
# Student should enter function on the next lines.

def name_and_age(name, age):
    return (str(name) +' is ' + str(age) +' years old.'
           if age > 0 else
           'Error: Invalid age')
###################################################
# Tests
# Student should not change this code.

print('Program 6:\n')

def test_6(name, age):
    """Tests the name_and_age function."""
    
    print (name_and_age(name, age))
    
test_6("Joe Warren", 52)
test_6("Scott Rixner", 40)
test_6("John Greiner", -46)

print('---------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe Warren is 52 years old.
#Scott Rixner is 40 years old.
#Error: Invalid age

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute and print tens and ones digit of an integer in [0,100).

###################################################
# Digits function
# Student should enter function on the next lines.

def print_digits(num):
    if num < 0 or num > 100:
        print ('Error: Input is not a two-digit number.')
    else:
        print ('The tens digit is '+ str(num//10)
            +', and the ones digit is '+ str(num%10)
            +'.')
    
###################################################
# Tests
# Student should not change this code.

print('Program 7:\n')

print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)

print('---------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.
#Error: Input is not a two-digit number.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute instructor's last name, given the first name.

###################################################
# Name lookup formula
# Student should enter function on the next lines.

def name_lookup(first_name):
    if (first_name == "Joe"):
        return 'Warren'

    if (first_name == "Scott"):
        return 'Rixner'

    if (first_name == "John"):
        return 'Greiner'

    if (first_name == "Stephen"):
        return 'Wong'
    
    return 'Error: Not an instructor'

###################################################
# Tests
# Student should not change this code.

print('Program 8:\n')

def test_8(first_name):
    """Tests the name_lookup function."""
    
    print (name_lookup(first_name))
    
test_8("Joe")
test_8("Scott")
test_8("John")
test_8("Stephen")
test_8("Mary")

print('---------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Warren
#Rixner
#Greiner
#Wong
#Error: Not an instructor

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute a (simplified) Pig Latin version of a word.

###################################################
# Pig Latin formula
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


###################################################
# Tests
# Student should not change this code.

print('Program 9:\n')

def test(word):
    """Tests the pig_latin function."""
    
    print (pig_latin(word))
    
test("pig")
test("owl")
test("python")

print('---------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#igpay
#owlway
#ythonpay

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the smaller root of a quadratic equation.

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.

def smaller_root(a, b, c):
    
    delta = b**2 - (4 * a *c)
    
    if delta < 0 or a == 0:
        print ("Error: No real solutions")
    else:
        discriminant_sqrt = delta ** 0.5
        # Choose the positive or negative square root that leads to a smaller root.
        if a > 0:
            smaller = - discriminant_sqrt
        else:
            smaller = discriminant_sqrt
        return (-b + smaller) / (2 * a)

###################################################
# Tests
# Student should not change this code.

print('Program 10:\n')

def test_10(a, b, c):
    """Tests the smaller_root function."""
    
    print ("The smaller root of " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " is:") 
    print (str(smaller_root(a, b, c)))
        

test_10(1, 2, 3)
test_10(2, 0, -10)
test_10(6, -3, 5)

print('---------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The smaller root of 1x^2 + 2x + 3 is:
#Error: No real solutions
#None
#The smaller root of 2x^2 + 0x + -10 is:
#-2.2360679775
#The smaller root of 6x^2 + -3x + 5 is:
#Error: No real solutions
#None

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
