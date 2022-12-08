from functools import reduce

with open("input") as f:
    inputMap = list(map(lambda x: list(map(lambda y: int(y), list(x))), f.read().split('\n')));

XMAX = len(inputMap[0]) - 1
YMAX = len(inputMap) - 1

def getNSEW(dimMap, x, y):
    return {
        "north": [dimMap[i][x] for i in range(0, y)],
        "south": [dimMap[i][x] for i in range(y + 1, YMAX + 1)],
        "east": [dimMap[y][i] for i in range(x + 1, XMAX + 1)],
        "west": [dimMap[y][i] for i in range(0, x)],
    }

def part1():
    visible = (XMAX * 2) + (YMAX * 2)
    
    for y in range(1, YMAX):
        for x in range(1, XMAX):
            thisTree = inputMap[y][x]
            adjecentTrees = getNSEW(inputMap, x, y)
            if max(adjecentTrees["north"]) < thisTree:visible += 1
            elif max(adjecentTrees["south"]) < thisTree:visible += 1
            elif max(adjecentTrees["east"]) < thisTree:visible += 1
            elif max(adjecentTrees["west"]) < thisTree:visible += 1
    print ("Part 1: All visible trees are:", visible)

def part2():
    scenicValues = []

    def higherTree(thisTree, trees):
        viewDist = 0
        for tree in trees:
            if tree < thisTree: viewDist += 1
            else: viewDist += 1; break
        return viewDist
    
    for y in range(1, YMAX):
        for x in range(1, XMAX):
            thisTree = inputMap[y][x]
            adjecentTrees = getNSEW(inputMap, x, y)
            score = list(filter(lambda x: x > 0, [
                higherTree(thisTree, reversed(adjecentTrees["north"])),
                higherTree(thisTree, adjecentTrees["south"]),
                higherTree(thisTree, adjecentTrees["east"]),
                higherTree(thisTree, reversed(adjecentTrees["west"]))
            ]))
            scenicValues.append(reduce(lambda a, b: a * b, score))
    print ("Part 2: Highest scenic value: ", max(scenicValues))

    
part1()
part2()