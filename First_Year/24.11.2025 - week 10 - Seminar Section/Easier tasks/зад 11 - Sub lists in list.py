#Задача 11: Напишете програма, която намира всички подсписъци на даден списък.

items = input("Enter anything (with spaces): ").split()
sub_lists = []

for start in range(len(items)):
    for end in range(start, len(items)):
        sub_lists.append(items[start:end+1])

print("Sub-Lists:", sub_lists)