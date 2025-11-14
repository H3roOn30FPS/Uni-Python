#Write a programme which detectes palindromes!

def is_palindrome(text):
    text = text.lower() #Lowers the letters
    text = text.replace(" ", "")    #Replaces the spaces/joins the seperated words 

    reversed_text = ""  #new variuble
    for char in text:
        reversed_text = char + reversed_text
    return text == reversed_text

anything = input("\nEnter anything: ")
print(is_palindrome(anything))