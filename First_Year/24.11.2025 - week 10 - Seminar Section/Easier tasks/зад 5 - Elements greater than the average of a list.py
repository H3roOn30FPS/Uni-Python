#Задача 5: Напишете програма, която намира всички елементи в списък, които са 
# по-големи от средната стойност на списъка.

user_input = input("Enter some numbers (with spaces): ")
full_list = user_input.split()
int_list = []
sum = 0

for j in full_list:
    int_list.append(int(j))
    sum += int(j)

average = sum / len(int_list)
list_greater = []

for i in int_list:
    if i > average:
        list_greater.append(i)
    
print("Full list: ", int_list)
print("Average:", average)
print(f"List of numbers greater than the average of the list: {list_greater}")