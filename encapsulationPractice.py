#
#
#
#               creating a protected class and private variable
#
#

class User:
        def __init__(self, user, password):
                self.__password=password #private
                self._username=user #protected
                
        def printThem(self):
                print("this is your user info")
                print("Your Password: {}".format(self.__password))
                print("Your Username: {}".format(self._username))




user1 = User("myUsername", "password123!")
user1.printThem()

                



