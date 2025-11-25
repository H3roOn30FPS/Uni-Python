#Задача 7: Напишете функция, която приема списък с числа като аргумент и връща най-голямото число в списъка. 

def highest (list_1):
    highest_num = 0
    inted_list = []
    
    for i in list_1:
        if int(i) > highest_num:
            highest_num = int(i)
    return highest_num


user_in = input("Enter me some numbers, will ya'?: ")
list_of_numbers = user_in.split()

print(f"Highest in the room: {highest(list_of_numbers)}")