#Прост Калкулатор

arithmetic_sign = str(input("Изберете функция (+, -, /, *): "))
a = float(input("Въведете число A: "))
b = float(input("Въведете число B: "))

if arithmetic_sign == "+":
    print("Сборът на числата a и b е:", a + b)
elif arithmetic_sign == "-":
    print("Разликата на числата a и b е: ", a - b)
elif arithmetic_sign == "/":
    print("Частното на числата a и b е: ", a / b)
elif arithmetic_sign == "*":
    print("Произведението на a и b е: ", a * b)
else:
    print("Възникна грешка! Опирайте отново!")