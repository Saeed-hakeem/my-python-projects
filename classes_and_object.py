class student:
    admission_number='' #pr
    student_name=''
    student_age=''
    def __init__(self,admission_number,student_name,student_age): #self makes reference tto our class assigning parameters to our class properties
        self.admission_number=admission_number
        self.student_name=student_name
        self.student_age=student_age
        print("student:",self.admission_number,self.student_name,self.student_age)
#class end
student1=student(100,"said",10) # instances of the cla
student2=student(101,"mercy",20)