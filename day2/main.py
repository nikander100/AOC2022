with open("input") as f:
    fContent = f.read();

scoreOne, scoreTwo = 0, 0;
gameTableOne = {"A": {"X": 4, "Y": 8, "Z": 3},
                "B": {"X": 1, "Y": 5, "Z": 9}, 
                "C": {"X": 7, "Y": 2, "Z": 6}};
gameTableTwo = {"A": {"X": 3, "Y": 4, "Z": 8},
                "B": {"X": 1, "Y": 5, "Z": 9}, 
                "C": {"X": 2, "Y": 6, "Z": 7}};
for inputLines in fContent.split("\n"):
    opponentHand, myHand = inputLines.split(' ');
    scoreOne += gameTableOne[opponentHand][myHand];
    scoreTwo += gameTableTwo[opponentHand][myHand];
print("ScoreOne:", scoreOne, "   ", "ScoreTwo:", scoreTwo);