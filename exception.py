"""
y=20
try:
    if x>20:
        print("x is greater than 20")
    else:
        print("x is less than 20")
except Exception as e:
    print("error:",e)
print("program ended")
"""
try:
    x=20
    print(x/y)
except Exception as e:
    print("error:",e)
print("program ended") #this line was executed