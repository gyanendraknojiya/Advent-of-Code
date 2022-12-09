def readInput():
    inputList = open("./input.txt", "r").readlines()
    return "".join(inputList)


input = readInput()
treeGrid = input.split("\n")

dataList = []

for row in treeGrid:
    dataList.append(list(row))


def column(matrix, i):
    return [row[i] for row in matrix]


def getViews(row, col, i, j):
    left, right = [row[:j], row[j+1:]]
    top, bottom = [col[:i], col[i+1:]]
    return [left, right, top, bottom]


noOfCols = len(dataList[0])
noOfRows = len(column(dataList, 0))


def puzzle1():
    outerTree = 2 * (noOfRows + noOfCols) - 4
    innerTreeVisible = 0
    for i in range(1, noOfRows-1):
        for j in range(1, noOfCols-1):
            treeHeight = dataList[i][j]
            treeRow = dataList[i]
            treeCol = column(dataList, j)
            views = getViews(treeRow, treeCol, i, j)
            for view in views:
                if (max(view) < treeHeight):
                    innerTreeVisible += 1
                    break
    return innerTreeVisible + outerTree


def puzzle2():

    highestScenicScore = 0
    for i in range(1, noOfRows-1):
        for j in range(1, noOfCols-1):
            treeHeight = int(dataList[i][j])
            treeRow = dataList[i]
            treeCol = column(dataList, j)
            views = getViews(treeRow, treeCol, i, j)
            left, right, top, bottom = views
            scenicScore = 1
            left.reverse()
            top.reverse()
            for view in [left, top, right, bottom]:
                score = 0
                for tree in view:
                    score += 1
                    if (int(tree) >= treeHeight):
                        break

                scenicScore = scenicScore * score
            if (scenicScore > highestScenicScore):
                highestScenicScore = scenicScore
    return highestScenicScore


print(puzzle1())
print(puzzle2())
