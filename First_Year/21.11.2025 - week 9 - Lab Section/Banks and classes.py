# Class Bank_Account: acc_num, holder_name, balance.
#     def acc_info (prints all the info)
#     def change_balance

# Create 5 account objects, add them to an List = acc_list,
# Create a function get_balance which looks for an account number and prints it.
# If it's not found, return "Account not found!"

class Bank_Account:
    def __init__(self, account_number, holders_name, balance):
        self.account_number = account_number
        self.holders_name = holders_name
        self.balance = balance
    
    def Account_Info(self):
        print(self.account_number, self.holders_name, self.balance)
    
    def Change_Balance(self):
        new_balance = input("Change balance to...:")
        self.balance = float(new_balance)

def Get_Balance(acc_list):
    accnumlookup = int(input("Enter number of Bank Account: "))
    for acc in acc_list:
        if acc.account_number == accnumlookup:
            acc.Account_Info()
            return
    print("Account not found!")


acc_1 = Bank_Account(33, "Stefan", 7005.64)
acc_2 = Bank_Account(44, "Daniel", 0.64)
acc_3 = Bank_Account(22, "David", 500.99)
acc_4 = Bank_Account(11, "Jarome", 1.99)
acc_5 = Bank_Account(7, "James Bond", 1000000.00)
dsk_bank = [acc_1, acc_2, acc_3, acc_4, acc_5]

acc_4.Account_Info()
acc_4.Change_Balance()
Get_Balance(dsk_bank)