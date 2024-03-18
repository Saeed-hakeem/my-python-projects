#creating a function
def is_even(number):
    if number % 2 == 0:
        print("even number")
    else:
        print("odd number")

    #calling a function
is_even(98)

#functions 2
def printEmobilis():
    for i in range(10):
        print(i+1,"Emobilis")

printEmobilis()

#dynamic illlustratiion of parameterised fuction
def printName(x):
    for i in range(10):
        print(x)

printName("said")

#default parameter
def printName(x="yankee"):
    for i in range(10):
        print(x)

printName()

#function 4
def getmodulus(y,x):
    return y%x

z=getmodulus(y=5,x=2)+99
print(z)

