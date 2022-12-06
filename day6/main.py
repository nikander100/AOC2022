with open("input") as f:
    fContent = f.read();

# Part1
for i in range(4, len(fContent)):
    print(len(set(fContent[i-4:i])))
    if len(set(fContent[i-4:i])) == 4:
        print(i)
        break

# Part2
for i in range(14, len(fContent)):
    if len(set(fContent[i-14:i])) == 14:
        print(i)
        break