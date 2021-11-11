import math

def one ():
    print(50+50)
    print(100-10)

def two():
    print(30+6)
    print(6^6)
    print(6**6)
    print(6+6+6+6+6+6+6)

def three():
    print("Hello World:10")


def four():
    principal = 800000
    
    mortgage = 10000
    r = .06
    i = 1

    while principal >  0:
          
          rate  = (principal  * r) / 12
          newP = (principal + rate) - mortgage
          row = "{}\t{}\t{}\t{}\t{}"
          if(newP <= 0):
                mortgage = principal + rate
                print(row.format(i,int(math.ceil(principal)),int(rate),int(mortgage),0))
          else: 
              print(row.format(i,int(principal),int(rate), int(mortgage), int(newP)))
          principal = newP
          i = i + 1



four()