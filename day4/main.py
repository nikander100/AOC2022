with open("input") as f:
    fContent = f.read();

overlap, overlapSet = 0, 0;
for inputLines in fContent.split("\n"):
    range1, range2 = inputLines.split(',');
    range1Start, range1End = map(int, range1.split('-'));
    range2Start, range2End = map(int, range2.split('-'));
    if (range1Start <= range2Start and range2End <= range1End) or (range2Start <= range1Start and range1End <= range2End):
        overlap += 1;
    if set(range(range1Start, range1End + 1)) & set(range(range2Start, range2End + 1)):
        overlapSet+= 1;
print("The overlaps are:", overlap);
print("The overlapping sets are:", overlapSet);