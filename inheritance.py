class Person:
    person_age=''
    person_name= ''
    person_residence= ''
    def __init__(self,person_age,person_name,person_residence):
        self.person_age=person_age
        self.person_name=person_name
        self.person_residence=person_residence
    
    def printPerson(self): #function to print properties
        print("Age:",self.person_age,"Name:",self.person_name,"Residence:",self.person_residence)

#inheritance from the parent class
class Student(Person):
    uniform=''
    def __init__(self,person_age,person_name,person_residence,uniform):
        super().__init__(person_age,person_name,person_residence)
        self.uniform=uniform

class teacher(Person):
    pay=0
    def __init__(self,person_age,person_name,person_residence,pay):
        super().__init__(person_age,person_name,person_residence)
        self.pay=pay

t1=teacher(100,"said","nairobi",200)
t1.printPerson()
print("pay:",t1.pay)
