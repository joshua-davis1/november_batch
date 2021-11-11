import random
import re

def one():
    nums = []
    for i in range(1500,2700):
        if i % 7 == 0 and i % 5 == 0:
            nums.append(i)
    print(nums)

def two():
    def convert_c_f(celsius):
        f = (celsius * 9/5) + 32
        print("%s f" % int(f))
    def convert_f_c(far):
        c = (far-32) * (5/9)
        print("%s c" % int(c))

    convert_c_f(50)
    convert_f_c(122)

def three():
    num = random.randint(1,9)
    while(True):
        print("Guess a number between 1 and 9.")
        guess = input()
        if int(guess) is num:
            print("Well guessed!")
            break

def four():
    x = "*"
    for i in range(1,3):
        for j in range(1,6):
            if i % 2:
                print(x*j)
            else:
                print(x*(5-j))

def six():
    i = input()
    print(i[:-1])

def seven():
    numList = [1,2,3,4,5,6,7,8,9]
    odd = 0
    even = 0
    for i in numList:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Number of even numbers: %s" % even)
    print("Number of odd numbers: %s" % odd)

def eight():
    datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    for i in datalist:
        s = re.findall("'([^']*)'", str(type(i)))[0].strip("'")
        print("type: {}, value: {}".format(s, i))


def nine():
    for i in range(7):
        if i == 3 or i == 6:
            continue
        print(i)

nine()