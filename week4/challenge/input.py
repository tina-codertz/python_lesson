# open and read the input file
with open('input.txt','r') as infile:
    content = infile.read()

    # count the number words in the content
    word_count = len(content.split())

    # convert the word to uppercase
    uppercase_content = content.upper()

    # write the processed text and. word count the output.txt
    with open('output.txt', 'w') as outfile:
        outfile.write(f'Word Count: {word_count}\n')
        outfile.write(uppercase_content)
        outfile.write('Processed content written to output.txt')


# print the word count
print('processing complete')
