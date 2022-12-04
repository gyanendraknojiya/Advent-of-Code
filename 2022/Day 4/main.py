def readInput():
    inputList = open('./input.txt', 'r').readlines()
    input = "".join(inputList)
    return input


input = readInput()
input = input.split("\n")


def makeAry(value):
    fValue, lValue = value.split("-")
    return [int(fValue), int(lValue)]


def isFullyContained(firstAry, secondAry):
    fStart, fEnd = firstAry
    sStart, sEnd = secondAry
    if (fStart <= sStart) & (fEnd >= sEnd):
        return True
    return False


def isContained(firstAry, secondAry):
    fStart, fEnd = firstAry
    sStart, sEnd = secondAry
    isStartContained = (fStart <= sStart) & (fEnd >= sStart)
    isEndContained = (fStart <= sEnd) & (fEnd >= sEnd)
    if (isStartContained | isEndContained):
        return True
    return False


def puzzle1():
    myScore = 0
    for pair in input:
        firstPair, secondPair = pair.split(',')
        firstAry = makeAry(firstPair)
        secondAry = makeAry(secondPair)
        isFirstPairContained = isFullyContained(firstAry, secondAry)
        if isFirstPairContained:
            myScore += 1
        else:
            isSecondPairContained = isFullyContained(secondAry, firstAry)
            if isSecondPairContained:
                myScore += 1
    return myScore


def puzzle2():
    myScore = 0
    for pair in input:
        firstPair, secondPair = pair.split(',')
        firstAry = makeAry(firstPair)
        secondAry = makeAry(secondPair)
        isFirstPairContained = isContained(firstAry, secondAry)
        if isFirstPairContained:
            myScore += 1
        else:
            isSecondPairContained = isContained(secondAry, firstAry)
            if isFirstPairContained | isSecondPairContained:
                myScore += 1
    return myScore


print(puzzle1())

print(puzzle2())
