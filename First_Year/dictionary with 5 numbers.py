#Ex.4: User inputs 5 numbers. Find the:1. sum of elements from 1st and 3rd index; 2. the avarage of those 5 numbers;
#3. make a dictionary where every number has the value of its opposite number(index-wise) 
# [for example: {1:5; 2:4; 3:3; 4:2; 5:1}]

numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(int(num))

#Sum of elements from index 1 and 3 
sum_1_to_3 = numbers[1] + numbers[3]

#Average of all 5 numbers
average = sum(numbers) / 5

#Create the "opposite number" dictionary
opposites = {}
for i in range(5):
    key = numbers[i]              # the number at index i
    value = numbers[4 - i]        # the opposite index (since we are fixed with 5 numbers only)
    opposites[key] = value

print("Numbers:", numbers)
print("Sum of index 1 to 3:", sum_1_to_3)
print("Average of all numbers:", average)
print("Opposite-index dictionary:", opposites)