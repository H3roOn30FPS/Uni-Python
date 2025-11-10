#Задача 1. Да се напише програма, която проверява дали потребителят въвел годините си (age) е пълнолетен.

Age = float(input('Enter your age:'))

if Age < 18:
    print(f'You are {int(Age)}, so you are underage!')
else:
    print("You are old! Wellcome! 1st drink on the house!")