#Задача 11. Направете програма, която намира първото нечетно число в интервал (start, end) въведен от потребителя и програмата спира, 
#           когато числото е намерено и изкарайте в конзолата съобщение: 
#           Първото четно число в интервала .. , .. е: ..
start = int(input("Enter start: "))
end = int(input("Enter end: "))

found = False

for i in range(start, end + 1):
    if i % 2 != 0:
        print(f"Първото нечетно число в интервала {start}, {end} е: {i}")
        found = True
        break

if not found:
    print(f"В интервала {start}, {end} няма нечетни числа.")