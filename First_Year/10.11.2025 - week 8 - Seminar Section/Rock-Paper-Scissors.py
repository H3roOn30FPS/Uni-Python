#Задача 15. Направете програма, която симулира игра на "Камък, ножица, хартия" срещу компютъра. 
#           Потребителят въвежда свой избор, а компютъра генерира случаен избор.
import random

print("Rock, Paper, Scissors")
print("----------------------")

user = input("Choose rock, paper or scissors: ").lower()

number = random.randint(1, 3)
if number == 1:
    computer = "rock"
elif number == 2:
    computer = "paper"
else:
    computer = "scissors"

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif user == "rock" and computer == "scissors":
    print("You win!")
elif user == "paper" and computer == "rock":
    print("You win!")
elif user == "scissors" and computer == "paper":
    print("You win!")
else:
    print("Computer wins!")

##########################################################################################################################
# Solution using lists
'''
import random

choices = ["камък", "ножица", "хартия"]
user_choice = input("Изберете камък, ножица или хартия: ")

if user_choice not in choices:
    print("Невалиден избор")
else:
    computer_choice = random.choice(choices)
    print(f"Компютърът избра: {computer_choice}")
    if user_choice == computer_choice:
            print("Равенство!")
    elif (user_choice == "камък" and computer_choice == "ножица") or \
            (user_choice == "ножица" and computer_choice == "хартия") or \
            (user_choice == "хартия" and computer_choice == "камък"):
            print("Поздравления! Вие печелите!")
    else:
            print("Компютърът печели!")
'''
