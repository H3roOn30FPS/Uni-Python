'''
Задача 9: Изчисление на дни, часове и минути:
    Напишете програма, която по въведени минути изчислява колко дни, часове и останали минути съответстват на този брой.
'''

minutes = int(input("Въведете брой минути: "))

days = minutes // 1440
minutes_left = minutes % 1440

hours = minutes_left // 60
minutes_left = minutes_left % 60

print(f"{days} дни, {hours} часа, {minutes_left} минути")