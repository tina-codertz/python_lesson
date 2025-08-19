student_id={112, 114, 116, 118, 115}
print('student id:', student_id)

# create a set of string type
vowel_letters = {'a','e','i','o','u'}
print('vowel letters:', vowel_letters)

# create a set of mixed data type
mixed_set={'hello',101, -2, 'bye'}
print('set of mixed data types:', mixed_set)


# create empty set in python

empty_set=set()

# create an empty dictionary

empty_dictionary={}

# check data type of empty_Set
print('data type of empty_set:',(empty_set))

# check data type of dictionary_set
print('data type of empty_dictionary',type(empty_dictionary))

# duplicate items in set
numbers ={2, 4, 6, 8, 10}
print(numbers)

# add and update set items in python

# adding items
numbers = {21, 34, 54, 12}
print('initial set:', numbers)

# using adding method add()
numbers.add(32)
print('updated set:', numbers)

# update()
companies = {"lacoste","google","apple"}
tech_companies=['ralph laureen','gucci']
companies.update(tech_companies)
print(companies)


# removing an element from set

languages = {'swift','java','python'}
print('initial set:',languages)

# remove java from list
removedValue=languages.discard('java')
print('set after remove():',languages)

# built in functions with set
# all(), any(), enumerate(),len(), max(),min(),sorted(),sum()


# iterate over a set in python
fruits = {'apple', 'peach','mango'}

for i in fruits:
    print(i)

    # finding number of sets elements
even_numbers = {2,4,6,8}
print('set:', even_numbers)
print('total elements:', len(even_numbers))

# union of two sets |

A={1, 3, 5}
B={0, 2, 4}

# perform union operation using
print('union using|:', A|B)

# perform union operation using union()
print("union using union():", A.union(B))



# set intersection

A={1, 2, 5}
B={1, 2, 3}

# Perform intersection &
print('intersection using &:', A & B)

# Perform intersection operation using intersection()
print('intersection using intersection():', A.intersection(B))




# set difference in python

A={2, 3, 5}
B={1, 2, 6}

# perform difference operation uisng &
print('difference using &:',A-B)

# PERFORM DIFFERENCE USING difference()
print('difference using difference():',A.difference(B))


# Set symmetric difference in python

A= {2, 3, 5}

B={1, 2, 6}
# perform difference operation
print("using^:", A^B)

# Using symmetric_difference():
print('using symmetric_difference():',A.symmetric_difference(B))


# check if sets are equal
A={1, 3, 5}
B={3, 5, 7}

# perform difference operation using &
if A == B:
    print('set A and set B are equal')

else:
    print('set A and B are not equal')