#User inputs 5 random numbers for the keyboard. Write a program that will: find the sum of those numbers

sumall = 0
for n in range (5):
    number = float(input("Enter a number: "))
    sumall += number
print(sumall)