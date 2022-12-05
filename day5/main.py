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
stack = [stackOne, stackTwo, stackThree, stackFour, stackFive, stackSix, stackSeven, stackEight, stackNine]

inputStacks, inputFile = fContent.split("\n\n")
for inputLine in inputFile.split("\n"):
	_, moveAmount, _, fromStack, _, toStack = inputLine.split(" ")
	for x in range(int(moveAmount), 0, -1):
		stack[int(toStack) - 1].append(stack[int(fromStack) -1].pop())
# for inputLine in stacks.split("\n"):
# 	for inputCrate in inputLine.split("  "):
# 		# if inputCrate == " ":
# 		# 	inputCrate.pop()
# 		print("["+inputCrate+"]")
# 	break;
for x in stack:
	print(x)

# ['B', 'L', 'F', 'S', 'V', 'R', 'S', 'L', 'H', 'V']
# ['W', 'J', 'B', 'P', 'J', 'M', 'F', 'P', 'W', 'M', 'R', 'R']
# ['F', 'W']
# ['V', 'S', 'C', 'B']
# ['V', 'J', 'H', 'J', 'M', 'H', 'S']
# ['Q', 'R', 'P', 'M', 'G', 'Z', 'Z', 'F']
# ['F', 'C', 'Q', 'L', 'P', 'T', 'V', 'W', 'Q', 'Z']
# ['N', 'W']
# ['M']