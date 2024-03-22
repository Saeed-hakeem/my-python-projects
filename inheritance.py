class Person:
    person_age=''
    person_name= ''
    person_residence= ''
    def __init__(self,person_age,person_name,person_residence):
        self.person_age=person_age
        self.person_name=person_name
        self.person_residence=person_residence

    def printPerson(self):
        print("Age:",self.person_age,"Name:",self.person_name,"Residence:",self.person_residence)

#inheritance from the parent class
class Student(Person):
    def __init__(self,person_age,person_name,person_residence):
        super().__init__(person_age,person_name,person_residence)