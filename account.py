# File for lab 12
class Account:
    def __init__(self, name: str):
        self.__account_name = name
        self.__account_balance = 0
        '''
        This function constructs the object and assigns default values
        
        :param name: Name of account
        '''
    def deposit(self, amount: int) -> bool:
        if(amount >= 0):
            bool = True
            self.__account_balance += amount
        else:
            bool = False
        '''
        This function deposits the defined amount of money into the account
        
        :param amount: Deposit amount
        :return: Boolean value for successful deposit or failure 
        '''
        return bool

    def withdraw(self, amount: int) -> bool:
        if(amount >= 0 and amount < self.__account_balance):
            bool = True
            self.__account_balance -= amount
        else:
            bool = False
        '''
        This function withdraws the defined amount of money from the account
        
        :param amount: Withdraw amount
        :return: Boolean value for successful withdraw or failure 
        '''
        return bool

    def get_balance(self) -> int:
        '''
        This function gets the account balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        This function gets the account name
        '''
        return self.__account_name

