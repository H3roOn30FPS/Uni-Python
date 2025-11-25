#Задача 6: Напишете програма, която намира всички елементи в списък, 
# които са по-малки от средната стойност на списъка, но по-големи от дадена стойност.


user_input = input("Enter some numbers (with spaces): ")
lower_num = int(input("Enter lower limit: "))
full_list = user_input.split()
int_list = []
sum = 0

for j in full_list:
    int_list.append(int(j))
    sum += int(j)

average = sum / len(int_list)
list_bellow = []

for i in int_list:
    if i < average and i > lower_num:
        list_bellow.append(i)
    
print("Full list: ", int_list)
print("Average:", average)
print(f"List of numbers bellow the average of the list and the set limit: {list_bellow}")