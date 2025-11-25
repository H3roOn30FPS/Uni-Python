#Задача 8: Напишете функция, която приема списък с числа като аргумент 
# и връща сумата на всички числа в списъка, които са по-големи от 10.

def sum_over_10(numbers):
    total = 0
    for num in numbers:
        if int(num) > 10:
            total += int(num)
    return total

user_in = input("Feed me some numbers (with spaces): ")
nums = user_in.split()
result = sum_over_10(nums)
print("Sum of numbers which are greater than 10:", result)