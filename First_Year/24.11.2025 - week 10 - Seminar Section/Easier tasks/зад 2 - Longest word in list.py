#Задача 2: Напишете програма, която намира всички думи в списък, които са по-дълги от 5 букви.
#apple, television, cat, important, dog python

user_input = input("Enter words: ")
words = user_input.split()
long_words = []
for w in words:
    if len(w) > 5:
        long_words.append(w)
print("List", words)
print("Думи по-дълги от 5 букви:", long_words)