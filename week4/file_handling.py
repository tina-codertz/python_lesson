# file handling ib pyhton is the ability to perform various operations on files like readign from and writing to them
# files are used to store data permanently unlike variables which lose their values when program ends 

# filws handling in python allows you to
# 1.open files
# 2.read and write data
# 3.close files 

# files operation in python
# opening files
# use python's built-in open() function to access files 
# syntax open(filename,mode) filename :name of the file mode:mode you want to open the file in
# modes includes "r":read mode "W":write mode "a":append mode "x":exclusive creation mode "b":binary mode "t":text mode  "rb":read binary mode "wt":write text mode

# example of opening a file in read mode
file = open('example.txt', 'r')

# reading files
# once a file is opened you can read its contents using methods like read(), readline(), and readlines()
# read() reads the entire file as a single string
# readline() reads a single line from the file
# readlines() reads all lines into a list
# example of reading a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)



# writing files
# to write data to a file you can use the write() or writelines() methods
# write() writes a string to the file
# writelines() writes a list of strings to the file
# example of writing to a file
with open('output.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.writelines(['Line 1\n', 'Line 2\n', 'Line 3\n'])


# closing files
# it's important to close files after you're done with them to free up system resources
# you can use the close() method or use a context manager (with statement) which automatically closes the file when done
# example of closing a file
file = open('example.txt', 'r')

# writing and appending to files
# to append data to an existing file use the 'a' mode
# this allows you to add new content without overwriting the existing data
# example of appending to a file
with open('output.txt', 'a') as file:
    file.write('This is an appended line.\n')


    # exception handling in file operations
    # basic structure 
    # try: runs code that may throw an errror
    # except: handles the error if it occurs
   
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")



    #  advanced errror handling with finally and custom
     # finally: runs code that should always execute, regardless of whether an error occurred
    #  custom exceptions/errors: you can define your own exception classes for specific error handling

try:
    file = open("sample.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()