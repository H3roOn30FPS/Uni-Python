#Задача 14. Направете програма, която генерира пирамида от числа.
rows = 4

for i in range(1, rows + 1):
    left = "".join(str(x) for x in range(1, i))
    right = "".join(str(x) for x in range(i, 0, -1))
    
    line = left + right
    print(line.center(rows * 2 - 1))
