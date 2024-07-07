# syntax => lamba args : expression

#lets create a function that adds 10 to any number
x = lambda a : a + 10
print(x(5))

y = lambda a, b : a * b
print(y(5, 10))

# using lambda with another function

def myFunc(n):
    return lambda a : a + n

x = myFunc(5)
print(x(10))
