'''
Q.2 Create an Account class Heirarchy 
Account with super class (acc_id, name, balance)
methods - withdraw and deposit

Create SavingsAccount as sub class of account - additional field (type - personal/corporate etc)
implement withdraw and deposit such that
- maximum upto 1 lakh can be deposited in an account at a time
- Min balance 5000 must be maintained while withdrawal (if type = corporate you withdraw full amount = balance)


Create CurrentAccount as sub class of account
implement withdraw and deposit such that
- maximum upto 2 lakh can be deposited in an account at a time
- Min balance 10000 must be maintained while withdrawal




Identify possible Exceptions and implement them'''


import MinimumBalanceError #import MiimumBalanceError


class Account:

    cnt = 1

    #creating a constructor
    def __init__(self, name, balance):
        self._id = Account.cnt
        self._name = name
        self._balance = balance

        Account.cnt+=1

    @property
    def get_balance(self):
        return self._balance

class SavingsAccount(Account):

    #constructor
    def __init__(self, name, balance, type):
        super().__init__(name, balance)
        self._type = type


    def withdraw(self, amount):
        if (self._type == 'personal'):
            min_balance = 500
        else:
            min_balance = 0

        if(self._balance - amount >= min_balance):
            self._balance = self._balance - amount
            print('amount withdrawn!!')
        else:
            print('Amount entered is less than balance amount!!')

    def deposit(self, amount):
        if (amount <= 100000):
            self._balance += amount
            print('amount deposited!!')
        
        else:
            print('amount more than 100000')



class CurrentAccount(Account):

    #constructor
    def __init__(self, name, balance):
        super().__init__(name, balance)

    
    def withdraw(self, amount):
        try:
            if(self._balance - amount >= 10000):
                self._balance = self._balance - amount
                print('amount withdrawn!!')
                print(self.get_balance)
        except MinimumBalanceError:
            print('Error: Amount entered is less than balance amount!!')

    def deposit(self, amount):
        if (amount <= 200000):
            self._balance += amount
            print('amount deposited!!')
            print(self.get_balance)
        
        else:
            print('amount more than 100000')
