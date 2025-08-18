# creating an empty_list
my_list=[]


# appending numbers
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("appended_list:",my_list)

# inserting 15 in my_list
my_list.insert(1,15)
print("inserted list:",my_list)

# extending my_list with new list
my_list.extend([50, 60, 70])
print('exteded list:',my_list)

# removing the last element
my_list.pop()
print("popped list:",my_list)

# sorting the list in ascending order
my_list.sort()
print("sorted list:",my_list)

# index of 30
position_of_30=my_list.index(30)
print(position_of_30)



