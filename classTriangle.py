# create a class that takes in three triangle values, A , B , and C
# properties a,b,c
# should use getters and setters
# has two additonal functions :
# 1.) get area
# 2.) calcluate the C value using pythagorean
from math import sqrt

class Triangle:

    def __init__(self, a, b, c=None ):
        self.A = a    # width
        self.B = b    # height
        self.C = c

    # Area of a triangle is 1/2 Base * Height
    def get_area(self):
        print("Height==", self.B )
        print("Width==" , self.A )
        area = (self.B * self.A )/2
        return area

    def set_C(self):
        self.C = sqrt( (self.A * self.A) + (self.B * self.B)  )



triangle3 = Triangle(1, 2)
print("A-", triangle3.A )
print("B-", triangle3.B)
print("C-", triangle3.C )  # None
triangle3.set_C()
print("A-", triangle3.A )
print("B-", triangle3.B)
print("C-", triangle3.C )  # None 

# # create a object called triangle1 and set its values to 2,4,6
# triangle1 = Triangle( 2, 4, 6)
# print("A-", triangle1.A )
# print("B-", triangle1.B)
# print("C-", triangle1.C )
#
# # print the area of triangle1
# print( triangle1.get_area() )
#
#
# triangle2 = Triangle( 5, 10, 3)
# print("A-", triangle2.A )
# print("B-", triangle2.B)
# print("C-", triangle2.C )
# # print the area of triangle2
# print( triangle2.get_area() )
#
