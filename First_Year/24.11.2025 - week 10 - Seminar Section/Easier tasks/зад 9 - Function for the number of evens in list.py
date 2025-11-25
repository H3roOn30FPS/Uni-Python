#Задача 9: Напишете функция, която приема списък с числа като аргумент и връща броя на четенните числа в списъка.

def count_of_evens(numbers):
    even_list = []
    for num in numbers:
        if int(num) % 2 == 0:
            even_list.append(int(num))
    return len(even_list)


user_in = input("Feed me some numbers (with spaces): ")
nums = user_in.split()
result = count_of_evens(nums)
print("Number of even numbers in the list:", result)