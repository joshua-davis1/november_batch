import math

# Question 1
# 1 - 9 == a - j

def oneA():
    print([1, 'word', 3.14])

def oneB():
    print([1, 1, [1,2]][2][1])

def oneC():
    print(['a','b','c'][1:])

def oneD():
    myDict = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    print(myDict)

def oneE():
    print({"k1":[1,2,3]}["k1"][1])

def oneF():
    tup = tuple([1,[2,3]])
    print(tup)

def oneG():
    print(set('Mississippi'))

def oneH():
    x = set('Mississippi')
    x.add('X')
    print(x)

def oneI():
    print(set([1,1,2,3]))

def oneJ():
    nums = []
    for i in range(2000, 3200):
        if i % 7 == 0 and i % 5 != 0:
            nums.append(i)
    return print(nums)

# Question 2
def two(input):
    return print(math.factorial(input))

def three(input):
    myDict = {}
    for i in range(1, input+1):
        if i == 0:
            continue
        myDict[i] = i**2

    return print(myDict)


def four(input):
    input = input.split(",")
    print(input)
    print(tuple(input))

class Five:
    def __init__(self):
        self.myStr = ""
    def getString(self, input):
        self.myStr = input
    def printString(self):
        print(self.myStr)

myClass = Five()
myClass.getString("some cool string")
myClass.printString()