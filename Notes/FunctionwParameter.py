

mySentence = 'loves the color'

color_list = ['red','blue','green','pink','black']


#name is a parameter
def color_function(name):
    lst = ['']
    for i in color_list:
        msg = '{0} {1} {2}'.format(name,mySentence, i)
        lst.append(msg)
    return lst #indentation shows return is INSIDE or OUTSIDE of the for loop


        

#input a name in the parenthesis and it
#will be concatenated to the function above
lst = color_function('Carolina')
for i in lst:
    print(i)
