#Ex. 2: User inputs a number s (3 > s < 6). then inputs s amount of numbers. The program creates one list with s amount of
#elements (example:s = 3; [21, 5, 17]). After that this list adds the sum of two adjacent numbers 
# (l1 = [21, 5, 17] = > [21, 26, 5, 22, 17]) (26 is sum of 21 and 5, and 22 is sum of 5 and 17.)

newn = None
while True:
    n = float(input("Input a real number (between 3 and 6): "))
    if n >= 3 and n <= 6:
        newn = int(n)
        break
    else:
        print("Error... Please enter a number between 3 and 6!\n")

numbers = []
for i in range(newn):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("Original list:", numbers)
i = 0
while i < len(numbers) - 1:
    sum_two = numbers[i] + numbers[i + 1]
    numbers.insert(i + 1, sum_two)
    i += 2   # skip over the number we just inserted
print("Final list:", numbers)

'''
#Colleague's take
for i in range(len(numbers)):
    if i % 2 == 0
        numbers.insert(i+1, (numbers[i] + numbers[i+1]))
print(numbers)
'''
