# function: a block
#  of code designed to perform a specific task. 
# you define a function once and can use it multiple
#  of times throughout your code

# syntax
def function_name(parameters):
    '''optional docstring explaining function'''
    # code block
    # return value optional return statement

    # types of functions
    # 1.built functions:predefined functions in python len() type()
    # 2.user-defined functions:functions created by the user


def greet(name):
    '''greet a person by their name'''
    return f'Hello, {name}!'

# function call
print(greet('Alice'))


# key components of function
# 1.function name:should be descriptive and follow naming conventions
# 2.parameterts:variables passed into the function
# 3.docstring:an optional description of what the function does
# return statement:output a value from the function(optional)

# positional arguments
def add(a, b):
    return a * b

print(add(3, 5))

# default arguments
def greet(name='guest'):
    return f'hello,{name}'
print(greet())
print(greet('Alice'))

# returning values
def square(number):
    return number ** 2
result = square(4)
print(result)

# anonymous functions:lambda- python supports functions uisng lambda keyword
add = lambda x, y : x + y
print(add(3, 5))

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)


# recursive function
# a function can call itself, enabling recursive problem-solving

def factorial (n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# benefits of functions
# reusabiliy
# modularity
# improved readability