#Задача 8. Напишете програма, която намира всички делители на въведено от потребителя число.
n = int(input("Enter a number: "))

print(f"Divisors of {n}:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
