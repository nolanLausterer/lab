# File for lab 12
class Account:
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        if(amount >= 0):
            bool = True
            self.__account_balance += amount
        else:
            bool = False

        return bool

    def withdraw(self, amount):
        if(amount >= 0 and amount < self.__account_balance):
            bool = True
            self.__account_balance -= amount
        else:
            bool = False

        return bool

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name

