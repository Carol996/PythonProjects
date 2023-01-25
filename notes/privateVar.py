
# private variable to ensure it's not changed by accident
class Numbers:
    def __init__(self):
        self.__privateEven = 2
        self._protectedOdd = 3

    def getPrivate(self):
        print(self.__privateEven)

    def setPrivate(self, newPvt):
        self.__privateEven = newPvt

obj = Numbers()
obj.getPrivate()
obj.setPrivate(12)
obj.getPrivate()
obj._protectedOdd = 33
print(obj._protectedOdd)

    
