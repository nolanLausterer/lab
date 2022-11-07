#Tester
from account import *

class Test:

    def setup_method(self):
        self.account1 = Account('joe')

    def teardown_method(self):
        del self.account1

    def test_init(self):
        assert self.account1.get_balance() == 0
        assert self.account1.get_name() == 'joe'

    def test_deposit(self):
        self.account1.deposit(200)
        assert self.account1.get_balance() == 200
        self.account1.deposit(-30)
        assert self.account1.get_balance() == 200
        assert self.account1.deposit(-30) is False

    def test_withdraw(self):
        self.account1.withdraw(50)
        assert self.account1.get_balance() == 0
        assert self.account1.withdraw(50) is False
        assert self.account1.withdraw(-10) is False
        self.account1.deposit(100)
        self.account1.withdraw(20)
        assert self.account1.get_balance() == 80

