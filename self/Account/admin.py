'''
Creare user class with user interface that gives 2 menu options
1. Deposit
2. Withdraw

Both options will ask user to enter money to withdraw/deposite
Display a statement with each transaction and final balance after user exits from the menu
'''

from account import CurrentAccount, SavingsAccount
from bank_app import Transaction


current = CurrentAccount('abc', 100000)

savings1 = SavingsAccount('khush', 100000, 'personal')
savings2 = SavingsAccount('pulkit', 200000, 'corporate')

trxn = Transaction()

# print("==========Menu==========")
# print("1. Deposite in Current account\n2. Deposite in Savings Account personal\n3. Deposite in Savings account corporate\n")

while(True):
    print("==========Menu==========")
    print("1. Deposite in Current account\n2. Deposite in Savings Account personal\n3. Deposite in Savings account corporate\n4. Withdraw from Current account\n5. Withraw from Saings account personal\n6. Withdraw from Savings account corporate\n7. Exit\n")
    ch = int(input("Enter choice: "))

    match ch:
        
        case 1:
            amount = int(input("Enter the amount to be deposited: "))
            trxn.deposite_to_account(current, amount)

        case 2:
            amount = int(input("Enter the amount to be deposited: "))
            trxn.deposite_to_account(savings1, amount)

        case 3:
            amount = int(input("Enter the amount to be deposited: "))
            trxn.deposite_to_account(savings2, amount)
        
        case 4:
            amount = int(input("Enter the amount to be withdrawn: "))
            trxn.withdraw_from_account(current, amount)

        case 5:
            amount = int(input("Enter the amount to be withdrawn: "))
            trxn.withdraw_from_account(savings1, amount)

        case 6:
            amount = int(input("Enter the amount to be withdrawn: "))
            trxn.withdraw_from_account(savings2, amount)
        
        case 7:
            print("Exitting...")
            break