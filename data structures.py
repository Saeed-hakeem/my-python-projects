"""
mystudents=["said","mercy","kimberly"]
print(mystudents)
mystudents.append("franco") #add item to list
print(mystudents)
mystudents.remove("mercy")   #remove item from list
print(mystudents)
mystudents[2]="franco madinka" #modify list
print(mystudents)


#empty list
students=[]
while len(students)<3:
  name_input= input("enter your students name:")
  students.append(name_input)

print(students)
"""

 #creating tuples
 mytuple=("said","mercy","nicole")
 #properties of a tuple
"""
1.tuples are immutable ie they cannot be changed directly
2.elements in a tuple are indexed
3.tuples are usually in round brackets
4.tuples  allow duplicates
5.tuples can have elements of diferrent data types
"""
print(mytuple[1])
mytuple[1]="mercy" #this will give an error because we cannot change tuple directly
print(mytuple[1])

#to modify /add/delete/delete tuples
"""
1.convert tuple into a list
  mylist=list(thetiplename)
2.modify the value you wanted the same way we did in list
    example on modification:
         student[0]="ken"
    example on deleting:
    student.remove(student[0])
    example on addiing:
    student.append("mercy")
3.convert it back into a tuple
mytuple=tuple(thelistname)

"""


