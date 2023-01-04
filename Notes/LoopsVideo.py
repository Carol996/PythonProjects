

mySentence = 'loves the color'

color_list = ['red','blue','green','pink','black']


#first function, tells me what is gonna be returned
def color_function(name):
    lst = ['']
    for i in color_list:
        msg = '{0} {1} {2}'.format(name,mySentence, i)
        lst.append(msg)
    return lst


#second function is used to create a loop         
def get_name():
    go = True
    while go:
        name = input ('what is your name? ')
        if name ==  '':
            print('you need to provide your name')
        elif name == 'Sally':
            print('Sally, you are not authorized to use this')
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)



get_name()
