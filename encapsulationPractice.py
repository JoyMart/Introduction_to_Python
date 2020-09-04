#
#
#
#               creating a protected class and private variable
#
#

class Protected:
        def __init__(self):
                self.__privateVar = 12
                
        def getPrivate(self):
                print(self.__privateVar)
                
        def setPrivate(self, private):
                self.__privateVar = private

                
obj = Protected()
obj.__protectedVar = 34
print(obj.__protectedVar)
obj.setPrivate(30)
obj.getPrivate()


#print(newNum.self.number1)
