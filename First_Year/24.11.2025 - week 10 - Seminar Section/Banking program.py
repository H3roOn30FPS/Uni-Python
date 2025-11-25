#Зад. 1 - Напишете програма, която да симулира работа с банкова сметка.


#-------------------#
#   Class Account   #
#-------------------#
class Account:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number
        self.balance = balance
        self.pin = pin
    
    def deposit(self, ammount):
        if ammount > 0:
            self.balance += ammount
            print(f"Successful transaction! New balance: {self.balance:.2f}")
        else:
            print(f"Please enter a positive value!\n\n")
        

    def withdraw(self, ammount, pin):
        if pin != self.pin:
            print("Wrong PIN number!\n\n")
            return

        if ammount <= 0:
            print("Error! Amount must be positive and greater than 0!\n\n")
            return
        
        if ammount > self.balance:
            print("Insufficient funds!\n\n")
            return

        self.balance -= ammount
        print(f"Withdraw successful! New balance: {self.balance:.2f}")

    def get_account_info(self):
        print(f"Account number: {self.account_number}")
        print(f"Balance: {self.balance:.2f}")


#----------------------------------#
#   Empty list for new Accounts    #
#----------------------------------#
accounts = []

def create_account():
    print("\n=== Open a new banking account ===")
    account_number = input("Enter account number: ")
    balance = float(input("Enter account balance: "))
    pin = input("Enter PIN code: ")

    acc = Account(account_number, balance, pin)
    accounts.append(acc)
    print("Account created successfully!\n")


def choose_account():
    if not accounts:
        print("No accounts available!\n")
        return None

    print("\n=== Select bank account ===")
    i = 0
    while i < len(accounts):
        acc = accounts[i]
        print(str(i + 1) + ". " + acc.account_number)
        i += 1

    choice = int(input("Choose from the list: ")) - 1

    if 0 <= choice < len(accounts):
        return accounts[choice]
    else:
        print("Error!")
        return None


#-------------------------#
#    Account adder body   #
#-------------------------#
while True:
    print("==================")
    print("Master menu")
    print("==================")
    print("1. Create new bank account")
    print("2. Select account")
    print("0. Exit")
    print("==================")

    option = input("Select operation: ")

    if option == "1":
        create_account()

    elif option == "2":
        acc = choose_account()
        if acc is None:
            continue


#----------------#
#    Main Body   #
#----------------#
        while True:
            print("==================")
            print("Option Menu:")
            print("==================")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Account information")
            print("0. Exit")
            print("==================")

            ch = input("Please select from the options above: ")

            if ch == "1":
                amount = float(input("Enter a deposit ammount: "))
                acc.deposit(amount)

            elif ch == "2":
                amount = float(input("Enter a withdraw ammount: "))
                pin_input = input("Enter PIN code: ")
                acc.withdraw(amount, pin_input)

            elif ch == "3":
                acc.get_account_info()

            elif ch == "0":
                break

            else:
                print("Error! Invalid operation!\n")

    elif option == "0":
        print("Exiting program...\n")
        break

    else:
        print("Error! Invalid operation!\n")