#Задача 16. Напишете програма, която чете от конзолата списък с числа и след това изчислява и отпечатва средната стойност на числата.

numbers = []
n = int(input("How many numbers would you like? "))

for i in range(n):
    num = float(input(f"Enter the {i + 1} number: "))
    numbers.append(num)

total = 0
for num in numbers:
    total += num

average = total / n

print("The Average sum is:", average)
