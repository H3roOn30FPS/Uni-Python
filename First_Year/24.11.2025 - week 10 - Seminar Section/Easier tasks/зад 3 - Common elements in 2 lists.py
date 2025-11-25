#Задача 3: Напишете програма, която намира всички елементи в списък, които са намерени и в друг списък.

input1 = input("Enter elements for the first list (separated by spaces): ")
list1 = input1.split()

input2 = input("Enter elements for the second list (separated by spaces): ")
list2 = input2.split()

common = []
for element in list1:
    if element in list2:
        common.append(element)

print("Common elements:", common)