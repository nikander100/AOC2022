import os

with open("input") as f:
    inputLines = f.read().split("\n");

def setupFileStruct(fileSystem):
    for line in range(len(fileSystem)):
        if "$ cd" in fileSystem[line]:
            cwd = os.getcwd()
            nDir = fileSystem[line].split(" ")[2]
            if nDir == "/":
                nDir = "root"
            nDirPath = os.path.join(cwd, nDir)
            os.chdir(nDirPath)
            cwd = os.getcwd()
            count = 1
            i = line + count
            newLine = fileSystem[i]
            while "$ cd" not in newLine:
                if "$ ls" in newLine:
                    pass
                elif newLine.startswith("dir"):
                    sDir = newLine.split(" ")[1]
                    sDirPath = os.path.join(cwd, sDir)
                    os.mkdir(sDirPath)
                else:
                    size, file = newLine.split(" ")
                    filePath = os.path.join(cwd, file)
                    with open(filePath, "w") as f:
                        f.write(size)
                count += 1
                i = line + count
                if i == len(fileSystem):
                    break
                newLine = fileSystem[i]

def getSize(paths):
    dirDict= {}
    dirPaths = [res[0] for res in os.walk(paths)]
    for path in dirPaths:
        dirName = path
        dirFiles = []
        for res in os.walk(path):
            dirFiles.extend([os.path.join(res[0], file) for file in res[2]])
        totalSize = 0
        for file in dirFiles:
            with open(file, "r") as f:
                totalSize += int(f.read().strip())
        dirDict[dirName] = totalSize
    return dirDict

def part1(root):
    dirDict = getSize(root)
    answer = 0
    for key in dirDict.keys():
        if dirDict[key] <= 100000:
            answer += dirDict[key]
    return answer

def part2(root):
    dirDict = getSize(root)
    sizes = [x[1] for x in dirDict.items()]
    sizes.sort()
    maxDir = sizes[-1]
    spaceLeft = 70000000 - maxDir
    updateSize = 30000000 - spaceLeft
    for x in sizes:
        if x >= updateSize:
            answer = x
            break
    return answer




root = os.path.join(os.getcwd(), "root")
# setupFileStruct(inputLines)

print("part1:", part1(root))
print("part2:", part2(root))