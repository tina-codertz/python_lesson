# create the inputs from user
numbers = input('enter numbers')

# # convert input string into list of intergers
numbers = list(map(int, numbers.split()))

total_sum= sum(numbers)
print("the sum is:", total_sum)


