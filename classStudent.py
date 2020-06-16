# You are assigned to design a class that stores student data
# The properties of the class include a name , ID number , and current grade value (number)



class Student:

        def __init__(self, n, i, gv):  # specific data
            self.name       = n    #set the data to the new object here
            self.ID         = i
            self.gradValue  = gv


object1 = Student("Thomas", 123, 96 )
object2 = Student("John",   456, 80 )
object3 = Student("Bob",   987,  60 )

# print the gradValue of John ?
print( object2.gradValue )
#print the id of Thomas ?
print( object1.ID )