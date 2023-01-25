#below is an example of a protected variable

class Odds:
    def __init__(self):
        self._protectedNum = 3

obj = Odds()
obj._protectedNum = 53
print(obj._protectedNum)

#the protected variable always equals to 3
#meaning it's encapsulated within that class
