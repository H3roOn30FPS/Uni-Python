#Задача 18. Напишете програма, която чете от конзолата списък с числа и след това го сортира по низходящ ред.
numbers = []

n = int(input("How many number are we working with? "))

for i in range(n):
    num = float(input(f"Number {i + 1}: "))
    numbers.append(int(num))

numbers.sort(reverse=True)
print("Списъкът сортиран по низходящ ред:", numbers)
