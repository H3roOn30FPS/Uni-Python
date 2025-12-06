#Зад. 1. 
'''
Напишете програма, в която се създава списък с 12 на брой елементи. 
•	Всеки елемент задължително трябва да бъде цяло положително число, въведено от потребителя.
•	Изведете броят на нечетните числа в списъка;
•	Намерете средноаритметичната стойност на числата в списъка.
•	Създайте втори списък, който да съхранява петте най-големи числа от първия списък, които са кратни на 2;
•	Сортирайте втория списък в низходящ ред;
•	Да се изтрият всички елементи от втория списък, които са с четен индекс.
'''

list_1 = [] #Empty list

while True: #inf loop untill condition is met
    n = 0   #Counter for the condition
    while n < 12:   #Condition: enter 12 elements
        user_input = float(input(f"Enter 12 numbers:"))  #Standard input
        if int(user_input) > 0: #Converts it into int type and checks if its positive
            list_1.append(int(user_input))  #Item get added to the list
            n += 1  #Counter goes up by 1 (only when the if condition is passed)
        else: #Quick error handler
            print("Number must be positive!!!") 
    break   #Stops the while True: loop in line 14
print("What's in List_1:",list_1)   #Printing results

#P.S.: We don't necessaraly need "while True:" and "break" since we have another "while" function inside

odd_num_count = 0   #Counter for the odd number in List_1
for n in list_1:    #For each elements in List_1
    if n % 2 == 1:  #Checks if it's an odd number
        odd_num_count += 1  #If so, counter goes up by 1
print("Odd numbers in List_1:", odd_num_count)  #Prints what've got

average = sum(list_1) / len(list_1) #Average sum in list
print("The Average of List_1 is:", average)  #Prints what've got

list_2 = [] #Another empty list
for n in list_1:    #For each and every element in List_1...
    if n % 2 == 0:  #...which is even (from List_1)...
        list_2.append(n)    #...we add it to List_2
print("What's in List_2:", list_2)    #Prints what've got

list_2.sort(reverse=True)   #We sort List_2 in Descending order by writing "reverse=True"
print("Sorted List_2 in Descending order:", list_2)  #Prints what've got

list_2 = list_2[:5] #We would like the have the first/top 5 biggest elements in List_2, so we cut the list till the 5th element
print("Top 5 biggest elements in List_2:", list_2)  #Prints what've got

#The Reverse Loop: for x in range(start, stop, step):
for i in range(len(list_2) - 1, -1, -1):    #For each index, in the ragnge of the lenght of List_2 - 1 
#(because indexes start from 0) as a top boundary/limit, then - 1 (the second one) defines the boundary/the bottom range or 
# tells the function to "Stop when you reach -1", - 1 (the 3rd) tells the function to "count backwards" or in other words we 
# start form the back of the list to check which numbers we need to exclude (in this case - the even numbers from List_2)
    if i % 2 == 0:  #If the index is even (2,4,6,8 ...)...
        list_2.pop(i)   #...We remove it

#del list_2[::2]    #Alternatively, this line just deletes the indexes by going 2 steps each time
print("List_2 with removed even indexes:", list_2)  #Prints what've got