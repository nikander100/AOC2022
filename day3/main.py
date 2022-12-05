with open("input") as f:
    fContent = f.read();

prio = 0;
for inputLine in fContent.split("\n"):
    half1 = inputLine[:len(inputLine)//2]
    half2 = inputLine[len(inputLine)//2:]
    for item in half1:
        if item in half2:
            value = ord(item) - 96 if item.islower() else ord(item) - 64 + 26;
            prio += value;
            break
    
prioTwo = 0;
tmp = [];
grouped = [];
for inputline in fContent.split("\n"):
    tmp.append(inputline)
    if len(tmp) == 3:
        grouped.append(tmp)
        tmp = [];

for group in grouped:
    for item in group[0]:
        if item in group[1] and item in group[2]:
            value = ord(item) - 96 if item.islower() else ord(item) - 64 + 26;
            prioTwo += value;
            break
print("Prio is:", prio, "PrioTwo is:", prioTwo);

