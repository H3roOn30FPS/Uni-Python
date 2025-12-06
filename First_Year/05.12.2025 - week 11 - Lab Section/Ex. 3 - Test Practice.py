#Зад. 3.
'''
Напишете програма, в която се създава списък с 20 на брой елементи. 
•	Всеки елемент задължително трябва да бъде цяло отрицателно число, избрано на случаен принцип.
•	Изведете най-голямото число от първия списък;
•	Намерете сумата на числата от първия списък.
•	Създайте втори списък, който да съхранява числата от първия списък, които са кратни на 3;
•	Сортирайте втория списък във възходящ ред;
•	Да се изтрият всички елементи от втория списък, които са с нечетен индекс. 
'''

#Task accurate approach:
'''
import random
import sys

ran_list = []
for i in range(20):
    ran_list.append(random.randint(-sys.maxsize, -1))
print ("The list of negative numbers", ran_list)
...

'''

# Normal/Reasonable approach
import random

ran_list = []
for i in range(20):
    ran_list.append(random.randint(-1000, -1))
print ("The list of negative numbers", ran_list)


biggest = ran_list[0]   #Futher from 0
lowest = ran_list[0]    #Closer to 0
#...
for b in ran_list:
    if b < biggest:
        biggest = b
    elif lowest < b:
        lowest = b
print("Biggest number:", biggest)
print("Lowest number:", lowest)

print("Total sum of list_1:", sum(ran_list))

list_2 = []
for n in ran_list:
    if n % 3 == 0:
        list_2.append(n)
print("List_2 (Elements devisible by 3):", list_2)

# list_2.sort(reverse=True)
# print("List_2 (sorted in descending order):", list_2)
list_2.sort() #reverse=False
print("List_2 (sorted in ascending order):", list_2)

for i in range(len(list_2) - 1, -1, -1):
    if i % 2 != 0:
        list_2.pop(i)
print("List_2 after removing odd indexes:", list_2)

# del list_2[::2]
# print("List_2 after removing odd indexes:", list_2)