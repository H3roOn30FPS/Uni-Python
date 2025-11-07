#Ex.3: User enters a string/characters. The program creates dictionary of those strings and gives them values
#equal to the times they are found in the input.

text = input("Enter a string: ")

dic_1 = {}
for ch in text:
    if ch in dic_1:
        dic_1[ch] += 1      # If it exists, increase the count
    else:
        dic_1[ch] = 1       # If it doesn't exist, add it with value 1

print("Character counts:", dic_1)