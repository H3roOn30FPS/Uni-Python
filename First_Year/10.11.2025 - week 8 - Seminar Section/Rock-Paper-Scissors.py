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
