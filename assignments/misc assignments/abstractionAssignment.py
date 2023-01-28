#import the ABC method from abc, as well as abstractmethod
from abc import ABC, abstractmethod


''' An ATM takes Deposits and gives out withdrawals
    they are always in the form of cash. Each method tells
    us what to do with the cash, and uses if/else statements
    to enforce conditions based on total cash amount.
'''

#parent class defines its method as abstract by 'mentioning' @abstractmethod
class Total(ABC):

    def Receipt(self, amount):
        print('Your total is: $',amount)
        
    

    @abstractmethod
    def Cash (self, amount):
        pass


class Purchase(Total):
    def Cash(self, amount):
        print('Your purchase has been completed successfully.')


obj = Purchase()
obj.Receipt(200)
obj.Cash(200)
