# simple calculator program


# enter the input

num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))
operation = input("enter the operation(+,-,*,/):")


# the calculations
if operation == "+":
    result = num1 + num2
    print(f"{num1}+{num2}={result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1}-{num2}={result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1}*{num2}={result}")

elif operation == "/":
    if num2 !=0:
        result = num1 / num2
        print(f"{num1}/{num2}={result}")
    else:
        print("error zero is not allowed")
else:
    print("invalid operation entered")

