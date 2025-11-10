#Задача 3. Напишете програма включваща оператор "elif", която изкарва в конзолата крайна оценка, спрямо подадените от потребителя точки.
#          Скала за оценяване: "Отличен 6" - 90 или повече, "Мн. Добър 5" - 80 или повече, "Добър 4" - 70 или повече, "Среден 3" - 60 или повече 
#          и "Слаб 2" под 60 точки.

grade = float(input("What did ya score?:"))

if grade > 90:
    print(f"You scored {grade} points, which means you got an Excellent(6) mark! Good job!")
elif grade > 80 and grade <= 90:
    print(f"You scored {grade} points, which means you got an Very Good(5) mark! Good job!")
elif grade > 70 and grade <= 80:
    print(f"You scored {grade} points, which means you got an Good(4) mark! Very nice!")
elif grade > 60 and grade <= 70:
    print(f"You scored {grade} points, which means you got an Fair(3) mark! Better luck next time!")
elif grade <= 60:
    print(f"You scored {grade} points, which means you got an Poor(2) mark! ... to the Electic chair!")
else:
    print(f"{grade} is invalid! Try again!")    #This else is not used