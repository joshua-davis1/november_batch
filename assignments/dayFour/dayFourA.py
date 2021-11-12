def one():
    print("Hello World")

# 2
def func1(name):
    print("Hi my name is %s" % name)

# 3
def func3(x,y,z):
    if z:
        return x
    return y

# 4
def func4(x,y):
    return x*y

# 5
def is_even(num):
    if num % 2 == 0:
        return True
    return False

# 6
def six(x,y):
    if x > y:
        return True
    return False

# 7
def seven(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

# 8
def eight(*args):
    evenList = []
    for i in args:
        if i % 2 == 0:
            evenList.append(i)
    return evenList

# 9
def nine(iStr):
    strList = []
    idx = 1
    for i in iStr:
        if idx % 2 == 0:
            strList.append(iStr[idx -1].upper())
        else:
            strList.append(iStr[idx -1].lower())
        idx+=1
    return "".join(strList)
        
# 10
def ten(x,y):
    if x % 2 == 0 and y % 2 ==0:
        if x < y:
            return x
        return y
    else:
        if x > y:
            return x
        return y

# 11
def eleven(sOne, sTwo):
    if sOne[0].lower() == sTwo[0].lower():
        return True
    return False

# 12
def twelve():
    print("Given a value,return a value which is twice as far as other side of 7")
    print("i dont understand?")

def thirteen(iStr):
    # A function that capitalizes first and fourth character of a word in a string.
    words = iStr.split(" ")
    r = []
    for word in words:
        s = word[0].upper()
        if len(word) == 1:
            r.append(s)
        elif len(word) > 1 and len(word) < 4:
            r.append(s + word[1:])
        else:
            r.append(s + word[1:3] + word[3].upper() + word[4:])    
            
    return " ".join(r)

print(thirteen("a yo bro code random tence support"))