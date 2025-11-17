#Задача 13. Направете програма, която намира всички комбинации от 3 различни числа в интервала от 1 до 9, чиято сума е 15.
for a in range(1, 10):
    for b in range(1, 10):    #alternatively range(a + 1, 10)        | this will print only
        for c in range(1, 10):    #alternatively range (b + 1, 10)   | the consecutive numbers which = 15
            if a != b and a != c and b != c:
                if a + b + c == 15:          
                    print(a, b, c)
