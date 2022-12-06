def readInput():
    inputList = open('./input.txt', 'r').readlines()
    input = "".join(inputList)
    return input


input = readInput()


def rotateList(ary):
    rotatedArray = []
    for index, r in enumerate(ary[0]):
        column = list(row[index] for row in ary)
        rotatedArray.append(list(filter(None, column)))
    return rotatedArray


def makeAry():
    stacksOfCrates, rearrangementProcedure = input.split("\n\n")
    stacksOfCrates = stacksOfCrates.replace("    ", ',').replace(" ", ",")
    stacksOfCrates = stacksOfCrates.split('\n')
    stacksOfCrates = stacksOfCrates[:len(stacksOfCrates) - 1]
    stacksOfCrates = stacksOfCrates[::-1]

    stacksOfCratesAry = []
    for stack in stacksOfCrates:
        stack = stack.split(",")
        stacksOfCratesAry.append(stack)

    stacksOfCratesAry = rotateList(stacksOfCratesAry)

    rearrangementProcedure = rearrangementProcedure.split("\n")
    rearrangementProcedureAry = []

    for rearrangements in rearrangementProcedure:
        rearrangements = rearrangements.replace("move ", "")
        rearrangements = rearrangements.replace(" from ", " ")
        rearrangements = rearrangements.replace(" to ", " ").split(" ")
        rearrangementProcedureAry.append(rearrangements)

    return stacksOfCratesAry, rearrangementProcedureAry


def shuffleStacks1(rearrangementProcedure, stacks):
    move, form, to = rearrangementProcedure
    move, form, to = int(move), (int(form) - 1), (int(to) - 1)
    moveFrom = stacks[form]
    breakPoint = len(moveFrom) - move
    toSave, toMove = moveFrom[:breakPoint], moveFrom[breakPoint:]
    stacks[form] = toSave
    # stack order
    toMove.reverse()
    stacks[to] = stacks[to] + toMove
    return stacks


def shuffleStacks2(rearrangementProcedure, stacks):
    move, form, to = rearrangementProcedure
    move, form, to = int(move), (int(form) - 1), (int(to) - 1)
    moveFrom = stacks[form]
    breakPoint = len(moveFrom) - move
    toSave, toMove = moveFrom[:breakPoint], moveFrom[breakPoint:]
    stacks[form] = toSave
    # QueueOrder
    stacks[to] = stacks[to] + toMove
    return stacks


def puzzle1():
    stacksOfCratesAry, rearrangementProcedureAry = makeAry()
    for rearrangement in rearrangementProcedureAry:
        stacksOfCratesAry = shuffleStacks1(rearrangement, stacksOfCratesAry)
    outputOrder = ""
    for stack in stacksOfCratesAry:
        stack = stack[-1].replace("[", '').replace("]", '')
        outputOrder += stack
    return outputOrder


def puzzle2():
    stacksOfCratesAry, rearrangementProcedureAry = makeAry()
    for rearrangement in rearrangementProcedureAry:
        stacksOfCratesAry = shuffleStacks2(rearrangement, stacksOfCratesAry)
    outputOrder = ""
    for stack in stacksOfCratesAry:
        stack = stack[-1].replace("[", '').replace("]", '')
        outputOrder += stack
    return outputOrder


print(puzzle1())

print(puzzle2())
