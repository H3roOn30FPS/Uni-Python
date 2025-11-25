#Задача 10: Напишете програма, която приема две думи и проверява дали те са анаграми 
# (имат едни и същи букви, но в различен ред).

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

'''
#Fast, easy, simple method

if sorted(word1.lower()) == sorted(word2.lower()):
    print("They are anagrams.")
else:
    print("They are NOT anagrams.")
'''


    # If lengths differ  not anagrams
if len(word1) != len(word2):
    print("Not anagrams")
else:
    # Turn the second word into a list so we can remove letters from it
    temp = []
    for ch in word2.lower():
        temp.append(ch)

    # Try to remove each letter of word1 from word2
    for ch in word1.lower():
        if ch in temp:
            temp.remove(ch)
        else:
            print("Not anagrams")
            break
    else:
        # If temp is empty - succesess
        if len(temp) == 0:
            print("Anagrams")
        else:
            print("Not anagrams")