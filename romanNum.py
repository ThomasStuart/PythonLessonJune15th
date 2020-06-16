# Write a Python class to convert an integer to a roman numeral

class numbers:

    # Properties        # 1
    def __init__(self, num ):
        List = ["I", "II", "III", "IV", "V"]
                #0    1      2     3     4
        self.number = num
        self.RN     = List[self.number-1]

object1 = numbers(1)
print("object1 - number:        ", object1.number )
print("object1 - roman numeral: ", object1.RN )

# object1  = 1  -> I
# object2  = 2  -> II
# 3  -> III
# 4  -> IV
# 5  -> V
# 6  -> VI
# 7  -> VII
# 8  -> VIII
# 9  -> IX
# 10 -> X
