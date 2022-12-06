def readInput():
    inputList = open("./input.txt", "r").readlines()
    input = "".join(inputList)
    return input


input = readInput()


def findMarker(noOfSeqs):
    a = 0
    while a < (len(input) - noOfSeqs):
        marker = input[a: a + noOfSeqs]
        if len(set([*marker])) > noOfSeqs - 1:
            return a + noOfSeqs
        else:
            a += 1


def puzzle1():
    return findMarker(4)


def puzzle2():
    return findMarker(14)


print(puzzle1())

print(puzzle2())
