class Person:
    person_age=''
    person_name= ''
    person_residence= ''
    def __init__(self):
        print("init person")

    def set_values(self,person_age,person_name,person_residence):
        self.person_age= person_age
        self.person_name= person_name
        self.person_residence= person_residence

    def display_values(self):
        print("The persons age is:",self.person_age,"The name is:",self.person_name,"The residence is:",self.person_residence)
    def printPerson(self):
         print("The persons age is:",self.person_age,"The name is:",self.person_name,"The residence is:",self.person_residence)
class Student(Person):
    def __init__(self,person_age,person_name,person_residence):
        super().__init__(person_age,person_name)

person1=Person()
person1.set_values(50,"kelvin","kiserian")
person1.display_values()