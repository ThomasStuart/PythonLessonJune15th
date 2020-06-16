# Write a Python class to find a pair of elements (indices of the two numbers)
# from a given array whose sum equals a specific target number. - Go to the editor
# Input:     numbers= [10,20,10,40,50,60,70], target=50
# Output: 3, 4


#  numbers       = [10,20,10,40,50,60,70]
#  adjacentSums  = [30, 30, 50, 90, 110, 130]
# pair = (3,4)



# properties:
#  1.  list of numbers
#  2.  adjacentSums
#  3.  target
#  4.  pair of index values where the elements combine to equal the target value

class findPair:

    def __init__(self, ln, t):
        self.ln          = ln
        self.adjacentSum = None  # we havent calculated
        self.target      = t
        self.pair        = None

    def asums(self):
        newList = []
        # hint: use a for loop to go through the ln list and sum the numbers
        # store them in the newList
        for i in range(0, len(self.ln)-1):
            sum = self.ln[i] + self.ln[i+1]
            newList.append(sum)
        self.adjacentSum = newList

    def findIndices(self):
        # traverse through the adjacent sum list and check to see if any numbers match the target
        # at the same time keep a index value for the pairs

       # self.adjacentSum =  [30, 30, 50, 90, 110, 130] , target = 50

        for i in range(0, len( self.adjacentSum ) ):

            # i == 0  -> self.adjacentSum[0] = 30    , if 30 == 50   ? No
            # i == 1  -> self.adjacentSum[1] = 30    , if 30 == 50   ? No
            # i == 2  -> self.adjacentSum[2] = 50    , if 50 == 50   ? yes

            # checking ? if they match the target number
            if self.adjacentSum[i] == self.target:
                # on the third iteration, we enter the clause
                self.pair = ( i, i+1)




                  # 0  1  2  3  4
# numbers1       = [10,20,10,40,50,60,70]
# adjacentSums1  = [30, 30, 50, 90, 110, 130]
# target1=50
# 2 , 3
object1  = findPair([10,20,10,40,50,60,70], 50)
object1.asums()
print( object1.adjacentSum )
object1.findIndices()
print( object1.pair )


                   # 0  1  2  3  4  5  6
#  numbers2       = [1, 2, 3, 4, 5, 6, 7]
#  adjacentSums2  = [3, 5, 7, 9, 11, 13]
#  target2 = 9
#  pair =  (3, 4)
object2  = findPair([1,2,3,4,5,6,7], 9)
object2.asums()
print( object2.adjacentSum )
object2.findIndices()
print( object2.pair )