

class User:
    #defs attributes of the class
    name = 'no name'
    email = ' '
    password = '123Bb'
    accnt = 0

    #defs the methods of the class
    def login(self):
        entry_email = input('enter email pls: ')
        entry_password = input('enter ur pword pls: ')
        if (entry_email == self.email and entry_password == self.password):
            print('welcome back {}'.format(self.name))
        else:
            print('you are not authorized to enter this page')

#outside of the class create an instance of the user class
newUser = User()


#call login method using the new object
newUser.login()
    
    
