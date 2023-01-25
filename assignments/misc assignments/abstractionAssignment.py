

#import the ABC method from abc, as well as abstractmethod
from abc import ABC, abstractmethod


''' An ATM takes Deposits and gives out withdrawals
    they are always in the form of cash. Each method tells
    us what to do with the cash, and uses if/else statements
    to enforce conditions based on total cash amount.
'''

#parent class defines its method as abstract by 'mentioning' @abstractmethod
class Total(ABC):
    @abstractmethod
    def Cash (self, amount):
        pass


#child class inherits Cash from parent abstract
class Withdrawal(Total):
    def Cash(self, amount):
        if amount > 500:
            print('Your withdrawal amount of {} exceeds the maximum withdrawal amount of $500.'.format(amount))
        else:
            print('Your withdrawal of {} has been completed. Thank you.'.format(amount))

#child class 2 inherits Cash from parent
class Deposit(Total):
    def Cash(self, amount):
        if amount > 1000:
            x = amount - 1000
            print('You can only deposit a maximum of 1000 per day. Please take the remaining {}.'.format(x))
        else:
            print('Your deposit of {} dollars has been completed. Thank you.'.format(amount))



obj = Deposit()
obj.Cash(400)

