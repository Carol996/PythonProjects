

#class 1
#This is the parent class
class Person:
    name = 'Lucas'
    pin = '1234'

    def getProfile(self):
        Pname = input('Name: ')
        Ppin = input('PIN: ')
        if (Pname == self.name and Ppin == pin):
            print('Welcome {}'.format(Pname))
        else:
            print('Sorry {}, check your PIN again')


#child1; inherits information from parent
class ph_rate(Person):
    name = 'Lucas'
    birth_month = '12'

    def getProfile(self):
        Pname = input('Name: ')
        BMonth = input('Birthday Month: ')
        if (Pname == self.name and BMonth == birth_month):
            print('Welcome {}'.format(Pname))
        else:
            print('Sorry {}, check your information again'.format(Pname))


#child2
#inherits information from parent
class c_rate(Person):
    name = 'Lucas'
    birthPlc = 'CA'

    def getProfile(self):
        Pname = input('Name: ')
        BPlc = input('In two letter format, type the state you were born in\nBirth Place: ')
        if (Pname == self.name and BPlc == birthPlc):
            print('Welcome {}'.format(Pname))
        else:
            print('Sorry {}, check your information again'.format(Pname))
    


#to invoke methods:

candidate = Person()
candidate.getProfile()


  
