#User inputs a number which needs to be > 1 and a whole. The program then creates a triangle.
newn = 0
while True:
    n = float(input("Enter a number: "))
    if n > 1 and n % 1 == 0:
        newn = int(n)
        break
    else:
        print("Error... Please enter new number!")
for i in range (newn):
    print("*" * (i + 1))

###

#My take
'''
number = int(input("Enter a number: "))
if number > 1:
    i = 1
    while i <= number:
        print("*" * i)
        i += 1
else:
    print("Error... Please enter new number!")
'''