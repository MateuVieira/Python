# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the number of feet corresponding to a number of miles.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
miles_1 = 13


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
miles_2 = 57


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
miles_3 = 82.67


###################################################
# Miles to feet conversion formula
# Student should enter formula on the next line.

feet = 5280

Result_1_1 = miles_1 * feet
Result_1_2 = miles_2 * feet
Result_1_3 = miles_3 * feet
###################################################
# Test output
# Student should not change this code.

print('---> Result 1:')
print('-----> {}  miles equals {} feet.'.format(miles_1,Result_1_1))
print('-----> {}  miles equals {} feet.'.format(miles_2,Result_1_2))
print('-----> {}  miles equals {:.2f} feet.'.format(miles_3,Result_1_3))
print('\n----------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#13 miles equals 68640 feet.

# Test 2 output:
#57 miles equals 300960 feet.

# Test 3 output:
#82.67 miles equals 436497.6 feet.
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the number of seconds in a given number of hours, minutes, and seconds.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
hours_1 = 7
minutes_1 = 21
seconds_1 = 37


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
hours_2 = 10
minutes_2 = 1
seconds_2 = 7


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
hours_3 = 1
minutes_3 = 0
seconds_3 = 1


###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter formula on the next line.

Result_1_1 = (((hours_1 * 60) + minutes_1) * 60) + seconds_1 
Result_1_2 = (((hours_2 * 60) + minutes_2) * 60) + seconds_2
Result_1_3 = (((hours_3 * 60) + minutes_3) * 60) + seconds_3


###################################################
# Test output
# Student should not change this code.

print('---> Result 2:')
print('-----> {} hours, {} minutes, and {} seconds totals to {} seconds.'
      .format(hours_1,minutes_1,seconds_1,Result_1_1))
print('-----> {} hours, {} minutes, and {} seconds totals to {} seconds.'
      .format(hours_2,minutes_2,seconds_2,Result_1_2))
print('-----> {} hours, {} minutes, and {} seconds totals to {} seconds.'
      .format(hours_3,minutes_3,seconds_3,Result_1_3))
print('\n----------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
# Test 1 output:
#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.

# Test 2 output:
#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.

# Test 3 output:
#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the length of a rectangle's perimeter, given its width and height.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
width_1 = 4
height_1 = 7


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
width_2 = 7
height_2 = 4


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
width_3 = 10
height_3 = 10

Result_1_1 = (2 * width_1) + (2 * height_1) 
Result_1_2 = (2 * width_2) + (2 * height_2) 
Result_1_3 = (2 * width_3) + (2 * height_3) 
###################################################
# Test output
# Student should not change this code.

print('---> Result 3:')
print('----->A rectangle {} inches wide and {}' 
      ' inches high has a perimeter of {} inches.'
      .format(width_1,height_1,Result_1_1))
print('----->A rectangle {} inches wide and {}' 
      ' inches high has a perimeter of {} inches.'
      .format(width_2,height_2,Result_1_2))
print('----->A rectangle {} inches wide and {}' 
      ' inches high has a perimeter of {} inches.'
      .format(width_3,height_3,Result_1_3))
print('\n----------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.

# Test 2 output:
#A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.

# Test 3 output:
#A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the area of a rectangle, given its width and height.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
width_1 = 4
height_1 = 7


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
width_2 = 7
height_2 = 4


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
width_3 = 10
height_3 = 10

Result_1_1 = width_1 * height_1 
Result_1_2 = width_2 * height_2
Result_1_3 = width_3 * height_3 

###################################################
# Test output
# Student should not change this code.

print('---> Result 4:')
print('----->A rectangle {} inches wide and {}' 
      ' inches high has an area of {} square inches.'
      .format(width_1,height_1,Result_1_1))
print('----->A rectangle {} inches wide and {}' 
      ' inches high has an area of {} square inches.'
      .format(width_2,height_2,Result_1_2))
print('----->A rectangle {} inches wide and {}' 
      ' inches high has an area of {} square inches.'
      .format(width_3,height_3,Result_1_3))
print('\n----------------------------------------------\n')


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.

# Test 2 output:
#A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.

# Test 3 output:
#A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the circumference of a circle, given the length of its radius.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.
PI = 3.14

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
radius_1 = 8


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
radius_2 = 3


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
radius_3 = 12.9


###################################################
# Circle circumference formula
# Student should enter formula on the next line.

Result_1_1 =  2 * radius_1 * PI 
Result_1_2 =  2 * radius_2 * PI 
Result_1_3 =  2 * radius_3 * PI 

###################################################
# Test output
# Student should not change this code.

print('---> Result 5:')
print('-----> A circle with a radius of {}' 
      ' inches has a circumference of {} inches.'
      .format(radius_1,Result_1_1))
print('-----> A circle with a radius of {}' 
      ' inches has a circumference of {} inches.'
      .format(radius_2,Result_1_2))
print('-----> A circle with a radius of {}' 
      ' inches has a circumference of {} inches.'
      .format(radius_3,Result_1_3))
print('\n----------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A circle with a radius of 8 inches has a circumference of 50.24 inches.

# Test 2 output:
#A circle with a radius of 3 inches has a circumference of 18.84 inches.

# Test 3 output:
#A circle with a radius of 12.9 inches has a circumference of 81.012 inches.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the area of a circle, given the length of its radius.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.
PI = 3.14

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
radius_1 = 8


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
radius_2 = 3


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
radius_3 = 12.9


###################################################
# Circle circumference formula
# Student should enter formula on the next line.

Result_1_1 =  PI * radius_1 ** 2
Result_1_2 =  PI * radius_2 ** 2
Result_1_3 =  PI * radius_3 ** 2

###################################################
# Test output
# Student should not change this code.

print('---> Result 6:')
print('-----> A circle with a radius of {}' 
      ' inches has a area of {} inches.'
      .format(radius_1,Result_1_1))
print('-----> A circle with a radius of {}' 
      ' inches has a area of {} inches.'
      .format(radius_2,Result_1_2))
print('-----> A circle with a radius of {}' 
      ' inches has a area of {} inches.'
      .format(radius_3,Result_1_3))
print('\n----------------------------------------------\n')


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A circle with a radius of 8 inches has an area of 200.96 square inches.

# Test 2 output:
#A circle with a radius of 3 inches has an area of 28.26 square inches.

# Test 3 output:
#A circle with a radius of 12.9 inches has an area of 522.5274 square inches.
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the future value of a given present value, annual rate, and number of years.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
present_value_1 = 1000
annual_rate_1 = 7
years_1 = 10


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
present_value_2 = 200
annual_rate_2 = 4
years_2 = 5


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
present_value_3 = 1000
annual_rate_3 = 3
years_3 = 20


###################################################
# Future value formula
# Student should enter formula on the next line.


Result_1_1 =  present_value_1 * (  (1 + (0.01 * annual_rate_1)) ** years_1)
Result_1_2 =  present_value_2 * (  (1 + (0.01 * annual_rate_2)) ** years_2)
Result_1_3 =  present_value_3 * (  (1 + (0.01 * annual_rate_3)) ** years_3)

###################################################
# Test output
# Student should not change this code.

print('---> Result 7:')
print('-----> The future value of ${} in {}' 
      ' years at an annual rate of {}% is ${}.'
      .format(present_value_1,years_1,annual_rate_1,Result_1_1))
print('-----> The future value of ${} in {}' 
      ' years at an annual rate of {}% is ${}.'
      .format(present_value_2,years_2,annual_rate_2,Result_1_2))
print('-----> The future value of ${} in {}' 
      ' years at an annual rate of {}% is ${}.'
      .format(present_value_3,years_3,annual_rate_3,Result_1_3))
print('\n----------------------------------------------\n')


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.

# Test 2 output:
#The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.

# Test 3 output:
#The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the statement about a person's name and age, given the person's name and age.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
name_1 = "Joe Warren"
age_1 = 52


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
name_2 = "Scott Rixner"
age_2 = 40


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
name_3 = "John Greiner"
age_3 = 46


###################################################
# Name and age formula
# Student should enter formula on the next line.

Result_1_1 =  name_1 + ' is ' +  str(age_1) + ' years old.'
Result_1_2 =  name_2 + ' is ' +  str(age_2) + ' years old.'
Result_1_3 =  name_3 + ' is ' +  str(age_3) + ' years old.'

###################################################
# Test output
# Student should not change this code.

print('---> Result 8:')
print('-----> ' + Result_1_1 )
print('-----> ' + Result_1_2)
print('-----> ' + Result_1_3)
print('\n----------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#Joe Warren is 52 years old.

# Test 2 output:
#Scott Rixner is 40 years old.

# Test 3 output:
#John Greiner is 46 years old.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the statement about a person's name and age, given the person's name and age.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
name_1 = "Joe Warren"
age_1 = 52


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
name_2 = "Scott Rixner"
age_2 = 40


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
name_3 = "John Greiner"
age_3 = 46


###################################################
# Name and age formula
# Student should enter formula on the next line.

Result_1_1 =  name_1 + ' is ' +  str(age_1) + ' years old.'
Result_1_2 =  name_2 + ' is ' +  str(age_2) + ' years old.'
Result_1_3 =  name_3 + ' is ' +  str(age_3) + ' years old.'

###################################################
# Test output
# Student should not change this code.

print('---> Result 9:')
print('-----> ' + Result_1_1 )
print('-----> ' + Result_1_2)
print('-----> ' + Result_1_3)
print('\n----------------------------------------------\n')
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#Joe Warren is 52 years old.

# Test 2 output:
#Scott Rixner is 40 years old.

# Test 3 output:
#John Greiner is 46 years old.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the distance between the points (x0, y0) and (x1, y1).

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
x0_1 = 2
y0_1 = 2
x1_1 = 5
y1_1 = 6


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
x0_2 = 1
y0_2 = 1
x1_2 = 2
y1_2 = 2


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
x0_3 = 0
y0_3 = 0
x1_3 = 3
y1_3 = 4


###################################################
# Distance formula
# Student should enter formula on the next line.

# Hint: You need to use the power operation ** .

result_10_1 = ( (( x0_1 - x1_1) ** 2) + (( y0_1 - y1_1) ** 2) ) ** 0.5
result_10_2 = ( (( x0_2 - x1_2) ** 2) + (( y0_2 - y1_2) ** 2) ) ** 0.5
result_10_3 = ( (( x0_3 - x1_3) ** 2) + (( y0_3 - y1_3) ** 2) ) ** 0.5

###################################################
# Test output
# Student should not change this code.

print('---> Result 10:')
print('-----> The distance from ({},{}) to' 
      ' ({},{}) is {}.'
      .format(x0_1,y0_1,x1_1,y1_1,result_10_1))
print('-----> The distance from ({},{}) to' 
      ' ({},{}) is {}.'
      .format(x0_2,y0_2,x1_2,y1_2,result_10_2))
print('-----> The distance from ({},{}) to' 
      ' ({},{}) is {}.'
      .format(x0_3,y0_3,x1_3,y1_3,result_10_3))
print('\n----------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#The distance from (2, 2) to (5, 6) is 5.0.

# Test 2 output:
#The distance from (1, 1) to (2, 2) is 1.41421356237.

# Test 3 output:
#The distance from (0, 0) to (3, 4) is 5.0.

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Compute the area of a triangle (using Heron's formula),
# given its side lengths.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
x0_1, y0_1 = 0, 0
x1_1, y1_1 = 3, 4
x2_1, y2_1 = 1, 1


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
x0_2, y0_2 = -2, 4
x1_2, y1_2 = 1, 6
x2_2, y2_2 = 2, 1


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
x0_3, y0_3 = 10, 0
x1_3, y1_3 = 0, 0
x2_3, y2_3 = 0, 10


###################################################
# Triangle area (Heron's) formula
# Student should enter formulas on the next lines.

a_1 = ( (( x0_1 - x1_1) ** 2) + (( y0_1 - y1_1) ** 2) ) ** 0.5
b_1 = ( (( x1_1 - x2_1) ** 2) + (( y1_1 - y2_1) ** 2) ) ** 0.5
c_1 = ( (( x0_1 - x2_1) ** 2) + (( y0_1 - y2_1) ** 2) ) ** 0.5

s_1 = 0.5 * ( a_1 + b_1 + c_1)

a_2 = ( (( x0_2 - x1_2) ** 2) + (( y0_2 - y1_2) ** 2) ) ** 0.5
b_2 = ( (( x1_2 - x2_2) ** 2) + (( y1_2 - y2_2) ** 2) ) ** 0.5
c_2 = ( (( x0_2 - x2_2) ** 2) + (( y0_2 - y2_2) ** 2) ) ** 0.5

s_2 = 0.5 * ( a_2 + b_2 + c_2)

a_3 = ( (( x0_3 - x1_3) ** 2) + (( y0_3 - y1_3) ** 2) ) ** 0.5
b_3 = ( (( x1_3 - x2_3) ** 2) + (( y1_3 - y2_3) ** 2) ) ** 0.5
c_3 = ( (( x0_3 - x2_3) ** 2) + (( y0_3 - y2_3) ** 2) ) ** 0.5

s_3 = 0.5 * ( a_3 + b_3 + c_3)

result_11_1 = (s_1 * (s_1 - a_1) * (s_1 - b_1) * (s_1 - c_1)) ** 0.5
result_11_2 = (s_2 * (s_2 - a_2) * (s_2 - b_2) * (s_2 - c_2)) ** 0.5
result_11_3 = (s_3 * (s_3 - a_3) * (s_3 - b_3) * (s_3 - c_3)) ** 0.5

###################################################
# Test output
# Student should not change this code.


print('---> Result 11:')
print('-----> A triangle with vertices ({},{}), ({},{}) and' 
      ' ({},{}) has an area of {}.'
      .format(x0_1,y0_1,x1_1,y1_1,x2_1,y2_1,result_11_1))
print('-----> A triangle with vertices ({},{}), ({},{}) and' 
      ' ({},{}) has an area of {}.'
      .format(x0_2,y0_2,x1_2,y1_2,x2_2,y2_2,result_11_2))
print('-----> A triangle with vertices ({},{}), ({},{}) and' 
      ' ({},{}) has an area of {}.'
      .format(x0_3,y0_3,x1_3,y1_3,x2_3,y2_3,result_11_3))
print('\n----------------------------------------------\n')

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.

# Test 2 output:
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.

# Test 3 output:
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
