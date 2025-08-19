capital_city = {
    "Nepal": "Kathmandu", 
    "Italy": "Rome",
    "England": "London"}

print(capital_city)


# testing dictionary
squares={1: 1, 3:9, 5:25, 7:49, 9:81}
print(1 in squares)
print(2 not in squares)

# membership test for key only not value
print(49 in squares)
 
squares={1:1, 3:9, 5:25, 7:49, 9:81}
for i in squares:
    print(squares[i])