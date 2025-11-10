#Задача 6. Напишете програма, която ще сумира всички числа от 1 до зададено от потребителя число n.

end_n = float(input("Enter a number:"))
sum_of = 0
for i in range(1, int(end_n) + 1):
    sum_of += i
print(sum_of)