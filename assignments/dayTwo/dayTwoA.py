import re


def one():
    print("Hello World"[-3])

def two():
    print("thinker"[2:5])
    print("hello"[1])

def three():
    print("Sammy"[2:])

def four():
    print(set("Mississippi"))

def five(input):
    flag = True
    input = "".join(re.split('[,.";!? ]', input)).lower()
    one = input[:len(input) // 2]
    two = input[len(input) // 2:]
    if len(two) > len(one):
        two = two[1:]
        
    i = 1
    for c in input:
        if c != input[-i]:
            flag = False
        i+=1
    return flag

print(five("O, a kak Uwakov lil vo kawu kakao!"))


