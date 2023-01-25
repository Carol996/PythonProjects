
# private variable to ensure it's not changed by accident
class Evens:
    def __init__(self):
        self.__privateEven = 2

    def getPrivate(self):
        print(self.__privateEven)

    def setPrivate(self, newPvt):
        self.__privateEven = newPvt

obj = Evens()
obj.getPrivate()
obj.setPrivate(12)
obj.getPrivate()
    
