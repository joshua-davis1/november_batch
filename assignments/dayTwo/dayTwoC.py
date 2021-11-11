def part_one():
    def crowd_test(crowd):
        if (len(crowd) > 3):
            print("This room is crowded!")

    nameList = ["Aleena", "Michele", "Mansa Musa", "Akbar"]
    crowd_test(nameList)
    nameList.pop()
    nameList.pop()
    print(nameList)
    crowd_test(nameList)

def part_two():
    def crowd_test(crowd):
        if (len(crowd) > 3):
            print("This room is crowded!")
        else:
            print("This room isn't very crowded...")

def part_three():
    def crowd_test(crowd):
        crowdSize = len(crowd)
        if (crowdSize is 0):
            print("This room is empty.") 
        elif (crowdSize < 3):
            print("This room is isn't very crowded...")
        elif (crowdSize < 6):
            print("This room is very crowded...")
        else:
            print("This room is being mobbed!")

    nameList = ["Aleena", "Michele", "Mansa Musa", "Akbar", "Jenny", "Marcus" ]

    crowd_test(nameList)


part_three()








