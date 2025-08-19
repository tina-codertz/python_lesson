# python library is a collection of pre-written code that you can use to perform common tasks without having to write everything from scratch

# how to use library in python
# import the library
import math
print(math.sqrt(16)) # using the sqrt function from the math library
print(math.pi) # using the pi constant from the math library

# importing part of a library
print('square root 36:', math.sqrt(36)) # using the sqrt function from the math library
print('pi value:', math.pi) # using the pi constant from the math library

# random library
import random 
print( random.randint(1, 10)) # using the randint function from the random library

# datetime library
import datetime

today = datetime.date.today() # get today's date
print('Today:', today)
print('Year:', today.year) # get the year from today's date
print('Month:', today.month) # get the month from today's date
print('Day:', today.day) # get the day from today's date

now = datetime.datetime.now() # get the current date and time
print('current time:', now.strftime('%H:%M:%S')) # format the time