

#class 1
#This is the parent class
class Person:
    name = 'Lucas'
    pin = '1234'

    def getProfile(self):
        Pname = input('Name: ')
        Ppin = input('PIN: ')
        if (Pname == self.name and Ppin == self.pin):
            print('Welcome {}'.format(Pname))
        else:
            print('Sorry {}, check your PIN again')


#child1; inherits information from parent
class ph_rate(Person):
    user = '00000'  #replaced 'name' with 'userID'
    birth_month = '12'

    def getProfile(self):
        User = input('User ID: ')
        BMonth = input('Birthday Month: ')
        if (User == self.user and BMonth == self.birth_month):
            print('Welcome')
        else:
            print('Sorry, check your information again')


#child2
#inherits information from parent
class c_rate(Person):
    codewrd = 'Penny' #replaced 'name' with 'codewrd'
    birthPlc = 'CA'

    def getProfile(self):
        CodeWrd = input('Code Word: ')
        BPlc = input('In two letter format, type the state you were born in\nBirth Place: ')
        if (CodeWrd == self.codewrd and BPlc == self.birthPlc):
            print('Welcome!')
        else:
            print('Sorry, check your information again')
    


#to invoke methods:

candidate = Person()
candidate.getProfile()


  
