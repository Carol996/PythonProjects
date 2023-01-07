#lambda is used as an anonymous function
#anonymous functions are single-functions
#they have no name, only one expression

def multiply(i):
    return i * i;
y = lambda x: x * x * x

print(y(20))
print(multiply(3))

#instead of defining a whole function
#we defined a variable as a lambda function
