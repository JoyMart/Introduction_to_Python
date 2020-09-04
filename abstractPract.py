#
#
#
#                       creating an abstraction method
#
#
#

from abc import ABC, abstractmethod


class books(ABC):
        def check(self, price):
                print("Your book purchase total: {}".format(price))
        @abstractmethod
        def payment(self, amount):
                pass


class giftCard(books):
        def payment(self, amount):
                print("Your purchase amount has exceeded your giftcard amount of {}.".format(amount))
        


obj = giftCard()
obj.check("$50")
obj.payment("$25")

