#Задача 4.  Да се напише програма, която проверете дали въведената от потребителя година е високосна.

leap_year = int(input("Enter a year:"))

if leap_year % 4 == 0:
    print(f"Year {leap_year} was a Leap Year!")
else:
    print(f"Year {leap_year} wasn't a Leap Year...")