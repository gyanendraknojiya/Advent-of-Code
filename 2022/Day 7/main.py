def readInput():
    inputList = open("./input.txt", "r").readlines()
    return "".join(inputList)


input = readInput()
data = input.split("\n")


def getCommand(cmd):
    if cmd == '$ ls':
        return 'show'
    elif '$ cd' in cmd:
        return 'move'
    elif 'dir' in cmd:
        return 'dir'
    else:
        return 'file'


def getPath(path, cmd):
    pathName = path
    if cmd == '$ cd /':
        pathName = 'root'
    elif cmd == '$ cd ..':
        pathName = "/".join(pathName.split('/')[:-1])
    else:
        cmdDir = cmd.split(' ')[-1]
        pathName += '/'+cmdDir
    return pathName


output = {}


def getDirSize(path):
    pathToMatch = ''
    isFound = False
    dirSize = 0
    for cmd in data:
        cmdType = getCommand(cmd)
        if (not isFound) & (cmdType == 'move'):
            pathToMatch = getPath(pathToMatch, cmd)
            if pathToMatch == path:
                isFound = True
        elif isFound:
            if path in output:
                dirSize += output[path]
                return dirSize
            elif cmdType == 'dir':
                dirName = cmd.split(' ')[-1]
                size = getDirSize(path+'/'+dirName)
                output[path+'/'+dirName] = size
                dirSize += size
            elif (cmdType == 'move'):
                return dirSize
            elif cmdType == 'file':
                dirSize += int(cmd.split(' ')[0])
    return dirSize


path = ''

for cmd in data:
    cmdType = getCommand(cmd)
    if (cmdType == 'move'):
        path = getPath(path, cmd)
        output[path] = getDirSize(path)


def puzzle1():
    totalSize = 0
    for size in output.values():
        if size < 100000:
            totalSize += size
    return totalSize


def puzzle2():
    totalSize = output['root']
    totalDiskSpace = 70000000
    requiredSpace = 30000000
    availableSpace = totalDiskSpace - totalSize
    spaceToDelete = requiredSpace - availableSpace
    fileToDelete = totalSize
    if spaceToDelete > 0:
        for size in output.values():
            if (size >= spaceToDelete) & (size <= fileToDelete):
                fileToDelete = size
    return fileToDelete


print(puzzle1())
print(puzzle2())
