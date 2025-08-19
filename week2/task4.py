set1 = input('enter your first set of numbers')
set2=input('enter your second list of numbers')

# convert input sets to intergers
set1= set(map(int, set1.split()))
set2= set(map(int, set2.split()))

# find common elements
new_set=set1.intersection(set2)
print('common elements:', new_set)