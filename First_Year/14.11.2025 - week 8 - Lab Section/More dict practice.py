#User inputs a number greater than 2. The programme creates a list from 1 to the inputed number.
#Then using the list it creates a dictionary with the reversed list as values (example: {1:3, 2:2, 3:1})

newn = None
while True:
    n = float(input("Input a real number (> 2): "))
    if n > 2:
        newn = int(n)
        break
    else:
        print("Error... Please enter a number greater than 2!\n")

def a_func (k):
    list_1 = list((range(1, k + 1)))
    print(list_1)
    dict_1 = {}
    rev_l = list_1 [::-1]
    for i in range(len(list_1)):
        dict_1[list_1[i]] = rev_l[i]
    print(dict_1)

a_func(newn)