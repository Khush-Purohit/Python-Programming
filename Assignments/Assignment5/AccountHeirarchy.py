from abc import ABC, abstractmethod

from Exceptions import *


class Account(ABC):

    def __init__(self,accid, name, balance):
        self.accid = accid
        self._name = name
        self._balance = balance

    @abstractmethod
    def withdraw (self, amount):
        pass
    
    @abstractmethod
    def deposite(self,amount):
        pass
    
    def showBalance(self):
        return self._balance

    def __str__(self):
        return f'Account id is {self._accid} name is {self._name} balance {self._balance}'

class SavingAccount(Account):
    def __init__ (self,accid, name, balance, type):
        Account.__init__(self,accid,name,balance)
        self._type = type


    def withdraw(self, amount):
        if(self._type == 'corporate'):
            if(amount <= self._balance):
                self._balance = self._balance - amount
                print('Amount withdrawn!!')    
        else:
            try:
                if(self._balance - amount >= 5000):
                    self._balance = self._balance - amount
                    print('Amount withdrawn!!')
                else:
                    raise MinimumBalanceLimit
                    # print('Cannot withdraw amount due to minimum balance limit')
            except:
                    print('\nCannot withdraw amount due to minimum balance limit!!\n')

    def deposite(self, amount):
        
        try:
            if(amount<=100000):
                self._balance+=amount
                print("Amount Deposited!!")

            else:
                raise AmountMoreThanMaxLimit
                # print("Max deposite limit is 100000")
        except:
            print('\nMaximum deposite Limit is 100000!!\n')




class CurrentAccount(Account):
    def __init__ (self,accid, name, balance):
        Account.__init__(self,accid,name,balance)


    def withdraw(self, amount):

        try:
            if(self._balance - amount >= 10000):
                self._balance = self._balance - amount
                print('Amount withdrawn!!')
            else:
                raise AmountMoreThanMaxLimit
                # print('Cannot withdraw amount due to minimum balance limit')

        except:
            print('\nCannot withdraw amount due to minimum balance limit!!\n')


    def deposite(self, amount):
        
        try:
            if(amount<=200000):
                self._balance+=amount
                print("Amount Deposited!!")

            else:
                raise MaxDepositeLimitReached
                # print("Max deposite limit is 200000")

        except:
            print("\nMax deposite limit is 200000!!\n")