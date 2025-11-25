#Задача 1: Напишете програма, която намира най-голямото число в списък.

user_input = input("Enter numbers: ")

parts = user_input.split()
numbers = []
for p in parts:
    numbers.append(float(p))   
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("The largest number is:", largest)