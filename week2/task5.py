# program to filter words with odd number of characters
words= ['apple','mango','pineapple','peach','onion']

# calculating length to get odd characters
odd_length_words=[word for word in words if len(word)%2 !=0]

# printing words
print("original words:",words)
print("words with odd numbers of characters:",odd_length_words)