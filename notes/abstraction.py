from abc import ABC, abstractmethod


class car(ABC):
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(car):
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit'.format(amount))

obj = DebitCardPayment()
obj.payment('$100')
