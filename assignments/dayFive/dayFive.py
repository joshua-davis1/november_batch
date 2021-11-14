class Person:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.bmi = weight / height **2
        self.size = ""
        self.setSize()

    def printBMI(self):
        print(self.bmi)

    def printAnswer(self):
        print(self.size)

    def setSize(self):
        if self.bmi <  18.5:
            self.size = "under"
        elif self.bmi < 25:
            self.size = "normal"
        elif self.bmi < 30:
            self.size = "over"
        else:
            self.size = "obese"


person1 = Person(80, 1.73)
person2 = Person(55, 1.58)
person3 = Person(49, 1.91)

person1.printAnswer()
person2.printAnswer()
person3.printAnswer()