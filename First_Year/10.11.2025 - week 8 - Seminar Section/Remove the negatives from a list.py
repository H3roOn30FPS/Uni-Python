#Задача 17. Напишете програма, която чете от конзолата списък с числа и след това премахва всички отрицателни числа от списъка.
a_list = []
n = int(input("How many numbers would you like? "))

for i in range(n):
    num = float(input(f"Number {i + 1}: "))
    a_list.append(int(num))

i = 0
while i < len(a_list):
    if a_list[i] < 0:
        a_list.pop(i)
    else:
        i += 1
print("Списък без отрицателни числа:", a_list)
