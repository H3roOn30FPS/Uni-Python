#Задача 2. Да се напише програма, която проверява дали въведеното от потребителя число е четно или нечетно. 

num = float(input("Enter a number:"))

if num % 2 == 0:
    print(f"The number {int(num)} is even!")
else:
    print(f"The number {int(num)} is odd!")