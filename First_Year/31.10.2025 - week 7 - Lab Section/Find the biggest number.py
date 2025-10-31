#User inputs n count of real positive even numbers. n is also chosen by the user. Find the biggest number of them all. 
newn = None
while True:
    n = float(input("How many numbers would you like to enter?: "))
    if n > 1 and n % 1 == 0:
        newn = int(n)
        break
    else:
        print("Error... Please enter new number!\n")

count = 1
big = 0
while count <= newn:
    numbers = float(input("Enter a number: "))
    if numbers > 0 and numbers % 2 == 0:
        if big < numbers:
         big = int(numbers)
        count += 1
    else:
        print("The number must be real, even and positive! Try again!")
print(f"The biggest number is: {big}")


###


#Colleague take
'''
newN = 0
while True:
    n = float(input("How many numbers would you like to enter?: "))
    if n > 1 and n % 1 == 0:
        newn = int(n)
        break
    else:
        print("Error... Please enter new number!\n")

biggestnumberYet = 0
for i in range (newN):
    while True:
        d = float(input("Въведете число: "))
        if d > 1 and d % 2 == 0:
            if d > biggestnumberYet
                biggestnumberYet = d
                break
            else:
                print("Error!")
    print(biggestnumberYet)
'''

#Professor's notes
'''
a = 0
NewN = 0
bN = 0
while True:
    n = float(input("Text"))
    if n > 1 and n % 1 == 0:
        NewN = int(n)
        while a < NewN:
            num = float(input("More text"))
            if num > 0 and num % 2 == 0:
                if num > bN
                bN = int(num)
            a += 1
        break
print(bN)
'''