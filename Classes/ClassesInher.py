

#creating a class w properties
class Student:
    def __init__(self, lname, fname):
        self.lastName = lname
        self.firstName = fname

#this method prints the props. above
    def printname(self):
        print(self.lastName, self.firstName)



#create an object using the class stated above
variable = Student('King','Martin')
variable.printname()


#child class numero 1
class Tutors(Student):
    pass


#child class numero 2
class Subj(Student):
    degree = 'Undergrad'
    alumni = True

