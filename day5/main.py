with open("input") as f:
	fContent = f.read();


stackOne   = ["W", "M", "L", "F"];
stackTwo   = ["B", "Z", "V", "M", "F"]
stackThree = ["H", "V", "R", "S", "L", "Q"]
stackFour  = ["F", "S", "V", "Q", "P", "M", "T", "J"]
stackFive  = ["L", "S", "W"]
stackSix   = ["F", "V", "P", "M", "R", "J", "W"]
stackSeven = ["J", "Q", "C", "P", "N", "R", "F"]
stackEight = ["V", "H", "P", "S", "Z", "W", "R", "B"]
stackNine  = ["B", "M", "J", "C", "G", "H", "Z", "W"]

stack = [stackOne.copy(), stackTwo.copy(), stackThree.copy(), stackFour.copy(), stackFive.copy(), stackSix.copy(), stackSeven.copy(), stackEight.copy(), stackNine.copy()]
stackPartTwo = [stackOne.copy(), stackTwo.copy(), stackThree.copy(), stackFour.copy(), stackFive.copy(), stackSix.copy(), stackSeven.copy(), stackEight.copy(), stackNine.copy()]

inputStacks, inputFile = fContent.split("\n\n")
for inputLine in inputFile.split("\n"):
	_, moveAmount, _, fromStack, _, toStack = inputLine.split(" ")
	for x in range(int(moveAmount), 0, -1):
		stack[int(toStack) - 1].append(stack[int(fromStack) -1].pop())
	for x in range(int(moveAmount), 0, -1):
		stackPartTwo[int(toStack) - 1].append(stackPartTwo[int(fromStack) -1].pop(-x))

print("Part 1")
for x in stack:
	print(x)
print()
print("Part 2")
for x in stackPartTwo:
	print(x)
