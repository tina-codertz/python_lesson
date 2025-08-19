# using single or double quotes for string
string = 'python programming'

# create a string using single quotes
string1="python programing"

# python string
name= "python"
print(name)

message= "i love python."
print(message)

# accessing string characters in python

greet="hello"
# access 1st index element
print(greet[1])


# strings are immutable
message= "hola amigos"

# assign new string to message variable
message="hello friends"
print(message);

# multiline string
message = '''
never gonna give you up
never gonna give you up
'''

print(message)


# string operations

#  comparison
str1 = "hello, world"
str2 = "i love python"
str3 = "hello, world"

# compare str1 and str2
print(str1==str2)
# compare str1 and str3
print(str1==str3)



# join two or more strings
greet= "hello"
name = "Jack"

# using + operator
result = greet + "" + name
print(result)


# iterate through python string
greet ="hello"
for letter in greet:
    print(letter)

# length
greet = "hello"
print(len(greet))

# string memmbership test

print("a" in" program")

# other methods upper,lower,partition,replace,find,split,index


# escape sequence in python
example = "he said, \"what's there?\""
print(example)

# python string formatting
name = "cathy"
country = "uk"
print(f'{name} is from {country}')