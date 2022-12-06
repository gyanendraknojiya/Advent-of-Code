scores1 = {
    "X": 1,  # rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissor
}

scores2 = {
    "X": 0,  # loose
    "Y": 3,  # draw
    "Z": 6,  # win
}

combinations1 = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3
}

combinations2 = {
    "AX": 3,  # loose
    "AY": 1,  # draw
    "AZ": 2,  # win

    "BX": 1,  # loose
    "BY": 2,  # draw
    "BZ": 3,  # win

    "CX": 2,  # loose
    "CY": 3,  # draw
    "CZ": 1  # win
}


def readInput():
    inputList = open('./input.txt', 'r').readlines()
    input = "".join(inputList)
    return input


input = readInput()
input = input.split("\n")


def puzzle1():
    myScore = 0
    for score in input:
        mySelection = score[-1]
        opponentScore = score[0]
        myPoints = scores1[mySelection]
        myScore += myPoints
        myScore += combinations1[opponentScore + mySelection]
    return myScore


def puzzle2():
    myScore = 0
    for score in input:
        mySelection = score[-1]
        opponentScore = score[0]
        myPoints = scores2[mySelection]
        myScore += myPoints
        myScore += combinations2[opponentScore + mySelection]
    return myScore


print(puzzle1())

print(puzzle2())
