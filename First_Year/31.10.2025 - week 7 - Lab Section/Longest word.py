#User input a sentence. Write a program that counts the words in it and output the longest word of all.
'''
sentence = str(input("What's on your mind?: "))

words = sentence.split()    #creates a list, but we can't use this in this task
word_count = 0
longest = ""

for word in words:
    word_count += 1
    if len(word) > len(longest):
        longest = word
print(f"Total word count is: {word_count}")
print(f"The loooooooongest words here is: {longest}")
'''

#Homework - find another way to do this task (without .split())!
sentence = str(input("What's on your mind?: "))
word_count = 0
longest_word = ""
current_word = ""

for ch in sentence:
    if ch != " ":
        current_word += ch
    else:
        if current_word != "":
            word_count += 1
            if len(current_word) > len(longest_word):
                longest_word = current_word
            current_word = ""
if current_word != "":
    word_count += 1
    if len(current_word) > len(longest_word):
        longest_word = current_word

print("Total word count is:", word_count)
print("The loooooooongest word here is:", longest_word)