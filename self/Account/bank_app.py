'''
Create Bank App with Transaction class
Create Method withdraw_from_account(account : Account)  and deposit_to_account(account : Account)
These methods will return the new balance after deposite/withdraw
'''

from account import Account


class Transaction:
    def withdraw_from_account(self,account : Account, amount):
        account.withdraw(amount)
        print(f"Current balance after transaction is : {account.get_balance}\n")
        # return
    
    def deposite_to_account(self,account  :Account, amount):
        account.deposit(amount)
        print(f"Current balance after transaction is : {account.get_balance}\n")
        # return