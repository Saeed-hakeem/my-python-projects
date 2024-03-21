class student:
    admission_number='' #properties of the class
    student_name=''
    student_age=''
    def __init__(self): #constructor function get calls by default whenever an object is created
        print("initialize student class")
    def set_name(self,student_name):
         self.student_name=student_name
    def display_name(self):
        print("The student name is:",self.student_name)


student1=student()
student1.set_name("mercy") #passing parameter
student1.display_name()
