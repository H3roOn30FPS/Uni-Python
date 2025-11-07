#Ex. 1: User inputs a real number > 1. The program then creates 2 tuples. The 1st one as the elements from 1 to the 
# inputed number. The 2nd tuple is the same as the 1st, but reversed 

newn = None
while True:
    n = float(input("Input a real number: "))
    if n > 1:
        newn = int(n)
        break
    else:
        print("Error... Please enter a number greater than 1!\n")

tuple_1 = tuple(range(1, newn + 1))     
tuple_2 = tuple_1[::-1]     #Slicing (reversing)

print("Tuple 1 is:",tuple_1)
print("Tuple 2 is:",tuple_2)