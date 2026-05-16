#Text Word Frequency Counter
#Input a piece of text.
#Output the number of times each word appears.
#Use a dictionary to store the counting results.
#Sort the output from highest frequency to lowest frequency.
#Ignore differences between uppercase and lowercase letters.

print("Welcome to the Text Word Frequency Counter!")

text = input("Please enter a piece of text: Can be multiple sentences or even a paragraph.\n")
text = text.lower()  # Convert to lowercase to ignore case differences
words = text.split()  # Split the text into words
word_count = {}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

# Sort the word count dictionary by frequency in descending order
sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)



print("\nWord Frequency:")
for word, count in sorted(word_count.items(), key=lambda item: item[1], reverse=True):
    print(f"{word}: {count}")   

