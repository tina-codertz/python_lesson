# creating a program that reads a file 
filename = input("Enter the filename to read: ")


try:
    # Try to open and read the file
    with open(filename, 'r') as file:
        data = file.read()
        print( data)


    with open('file_output.txt', 'w') as output_file:
        modified_data = data.upper()
        output_file.write(modified_data)
        print("Data written to file_output.txt")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")