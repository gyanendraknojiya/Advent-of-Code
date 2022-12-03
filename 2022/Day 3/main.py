def charPriority(letter):
    if letter.isupper():
        return ord(letter) - 38
    return ord(letter) - 96


def readInput():
    inputList = open('./input.txt', 'r').readlines()
    input = "".join(inputList)
    return input


input = readInput()
input = input.split("\n")


def puzzle1():
    myScore = 0
    for compartment in input:
        firstCompartment, secondCompartment = compartment[:len(compartment)//2], compartment[len(compartment)//2:]
        commonCompartment = list(set(firstCompartment) & set(secondCompartment))
        myScore += charPriority(commonCompartment[0])
    return myScore


def puzzle2():
    myScore = 0
    setOfThree = []
    for compartment in input:
        setOfThree.append(compartment)
        if len(setOfThree) == 3:
            firstCompartment, secondCompartment, thirdCompartment = setOfThree
            commonCompartment = list(set(firstCompartment) & set(secondCompartment) & set(thirdCompartment))
            myScore += charPriority(commonCompartment[0])
            setOfThree = []
    return myScore


print(puzzle1())

print(puzzle2())
