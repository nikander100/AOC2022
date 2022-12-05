with open("input") as f:
	fContent = f.read();

inputStacks, inputFile = fContent.split("\n\n")

# Stack Creator
stackInput = []
stackInputRow = []
for inputLine in inputStacks.split("\n"):
	for x in range(1, 34, 4):
		stackInputRow.append(inputLine[x])
		if stackInputRow[-1] == " ":
			stackInputRow[-1] = ""
	stackInput.append(stackInputRow)
	stackInputRow = []
stackInput.pop()

stacks = [[]for _ in range(9)]
stacksPartTwo = [[]for _ in range(9)]
for inputSortedLine in reversed(stackInput):
	for j, crate in enumerate(inputSortedLine):
		stacks[j].append(crate)

for i, stack in enumerate(stacks):
	stacks[i] = [x for x in stack if x]
	stacksPartTwo[i] = [x for x in stack if x]

# # PushSwap
for inputLine in inputFile.split("\n"):
	_, moveAmount, _, fromStack, _, toStack = inputLine.split(" ")
	for x in range(int(moveAmount), 0, -1):
		stacks[int(toStack)].append(stacks[int(fromStack)].pop())
	break
	for x in range(int(moveAmount), 0, -1):
		stacksPartTwo[int(toStack) - 1].append(stacksPartTwo[int(fromStack) -1].pop(-x))

# Output
print("Part 1")
for x in stack:
	print(x)
print()
print("Part 2")
for x in stacksPartTwo:
	print(x)
