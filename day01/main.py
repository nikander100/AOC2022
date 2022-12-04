with open("input") as f:
    fContent = f.read();

elfTotal = [];

for elfCals in fContent.split("\n\n"):
    total = sum([int(x) for x in elfCals.split("\n")]);
    elfTotal.append(total);

print("Max cals:", max(elfTotal));
elfTotal.sort();
print("Top 3 max cals:", sum(elfTotal[-3:]));