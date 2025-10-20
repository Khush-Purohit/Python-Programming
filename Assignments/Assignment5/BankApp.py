from AccountHeirarchy import *


class Transaction():
    def __init__(self):
        pass

    def withdraw_from_account(self,account : Account, amount):
        account.withdraw(amount)
    
    def deposit_to_account(self,account : Account, amount):
        account.deposite(amount)

    def showBalance(self,account,accountName):
        return f'\nUpdated balance of {accountName} is {account.showBalance()}\n'