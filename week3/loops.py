# for loop
# indefinite iteration
# definite iteration

# for loop
# perform an action on each element

fruits = ['apple','banana','cherry']
for fruit in fruits:
    print(f'i love {fruits}')

# using range

for number in range(1,6):
    # print(f"number:{number}")
    print(number)


# while loop
# perform a set of instructions as long as the given condition is true
count = 1
while count <=5:
    print(f'count:{count}')
    count +=1



# loop controls
for number in range(1,10):
    if number == 8:
        print("breaking the loop at 8")
        break
    elif number % 2==0:
        print(f"skipping{number} because its even")
        continue
    print(f"processing number:{number}")


    # continue statement

    # nested loop
    for i in range(1,4):
        for j in range(1, 4):
            print(f"outer loop:{i}, inner loop:{j}")


# nested loops

for i in range(1, 4):
    for j in range(1, 4):
        print(f"outer loop: {i}, inner loop:{j}")
    

#  list comprehensions
#  syntax:
#  [expression for item in iterable if conditional]
# expression:the value or transformation applied to each element
# item:a variable that represents each element in the iterable
# condition:optional a filter  that determines whether to include element


# tradiditional loop
squares = []
for x in range(5):
    squares.append(x**2)

# list comprehension
squares = [x**2 for x in range(5)]
print(squares)



# nested list comprehensions
# create a 3 x 3 matrix using nested list comprehensions
matrix=[[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)


# transforming data
names = ["Alice","Bob","Charles"]
uppercased_names=[name.upper() for name in names]
print(uppercased_names)

# filtering data
numbers = [10,15,20,25,30]
divisible_by_5=[num for num in numbers if num % 5 == 0]
print(divisible_by_5)

# flattening a list
nested_list=[[1,2],[3,4],[5,6]]
flat_list=[item for sublist in nested_list for item in sublist]
print (flat_list)

# advantages of list comprehensions
# conciseness
# readability
# performance


# when not to use list comprehensions
#in too complex cases its more approprate in traditional loops or generator function

# complex list comprehensions
result = [x * y for x in range (10) for y in range (5) if x + y >5]

# better as a loop more readable
result = []
for x in range (10):
    for y in range(5):
        if x + y > 5:
            result.append(x * y)

print(result)            


# conclusion:list comprehensions are versatile and effficient tool, enabling you to write cleaner and faster code