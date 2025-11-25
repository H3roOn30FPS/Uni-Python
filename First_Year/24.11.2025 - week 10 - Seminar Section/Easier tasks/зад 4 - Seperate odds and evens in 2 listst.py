#Задача 4: Напишете програма, която разделя списък на два списъка, единият с четни, а другият с нечетни числа.

user_input = input("Enter some numbers (with spaces):")

list_of_all = user_input.split()
list_of_evens =[]
list_of_odds = []

for i in list_of_all:
    if int(i) % 2 == 0:
        list_of_evens.append(i)
    else:
        list_of_odds.append(i)

print(f"List of odd numbers: {list_of_odds}")
print(f"List of even numbers: {list_of_evens}")