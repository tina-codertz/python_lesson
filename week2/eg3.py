# add elements to python list

# append()
numbers=[21,34,54,12]
print("Before Append:",numbers)

# using apend method
numbers.append(32)

print("After Append:",numbers)


# using extend()

prime_numbers=[2,3,5]
print("List1:",prime_numbers)

even_numbers=[4,6,8]
print("List2:",even_numbers)

# join two lists
prime_numbers.extend(even_numbers)
print("List after append:",prime_numbers)


# Remove an item from list

# usingg del()

languages=['python','swift','c++','c','java','rust','r']

del languages[1]
print(languages)

del languages[-1]
print(languages)

del languages[0:2]
print(languages)



# using remove(
languages=['python','swift','c','java']
languages.remove('python')
print(languages)

# iterating through list

languages=['python','swift','c++']

for language in languages:
    print(language)




 # list comprehension

numbers= [number*number for number in range(1,6)]

print(numbers)

number=[numbers*x for x in range(1,6)]
print(numbers)