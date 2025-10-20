from AccountHeirarchy import *
from BankApp import Transaction

class User:
    saving = SavingAccount(1,'aa',10000,'corporate')
    current = CurrentAccount(2,'bb',20000)
    o1 = Transaction()

    # print(saving)
    # print(current)
    while(True):

        print('\n=========USER=========')
        print('1. Deposite in current account \n2. Deposite in savings account \n3. Withdraw from current account \n4. Withdraw from savings account \n5. Show balance of saving account \n6. Show balance of current account \n7. Quit \n')
        ch = int(input(("Enter the choice in integer: ")))

        match ch:
            case 1:
                amount = int(input("Enter the amount to deposite: "))
                o1.deposit_to_account(current,amount)
                print(o1.showBalance(current,'current account'))


            case 2:
                amount = int(input("Enter the amount to deposite: "))
                o1.deposit_to_account(saving,amount)
                print(o1.showBalance(saving,'saving account'))

            case 3:
                amount = int(input("Enter the amount to be withdrawn: "))
                o1.withdraw_from_account(current,amount)
                print(o1.showBalance(current,'current account'))

            case 4:
                amount = int(input("Enter the amount to be withdrawn: "))
                o1.withdraw_from_account(saving,amount)
                print(o1.showBalance(saving,'current account'))

            case 5:
                print(o1.showBalance(saving, 'saving account'))

            case 6:
                print(o1.showBalance(current, 'current account'))

            case 7:
                break

            case _:
                print("Enter a valid choice!!\n")