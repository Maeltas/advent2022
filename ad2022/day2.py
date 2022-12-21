points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "win": 6,
    "loss": 0,
    "draw": 3
}
map={
    "X": "win",
    "Y": "draw",
    "Z": "loss"
}
f = open("day2.input", "r")
pts=0
score=0
for l in f:
    l = l.split()
    if l[0]=="A":
        if l[1]=="X":
            pts+=points["draw"]+points[l[1]]
        elif l[1]=="Y":
            pts += points["win"] + points[l[1]]
        else:
            pts += points["loss"] + points[l[1]]
    elif l[0]=="B":
        if l[1]=="X":
            pts+=points["loss"]+points[l[1]]
        elif l[1]=="Y":
            pts += points["draw"] + points[l[1]]
        else:
            pts += points["win"] + points[l[1]]
    elif l[0] == "C":
        if l[1] == "X":
            pts += points["win"] + points[l[1]]
        elif l[1] == "Y":
            pts += points["loss"] + points[l[1]]
        else:
            pts += points["draw"] + points[l[1]]
    if l[0]=="A":
        if l[1]=="X":
            score+=points["loss"]+points["Z"]
        elif l[1]=="Y":
            score += points["draw"] + points["X"]
        else:
            score += points["win"] + points["Y"]
    elif l[0]=="B":
        if l[1]=="X":
            score+=points["loss"]+points["X"]
        elif l[1]=="Y":
            score += points["draw"] + points["Y"]
        else:
            score += points["win"] + points["Z"]
    elif l[0] == "C":
        if l[1] == "X":
            score += points["loss"] + points["Y"]
        elif l[1] == "Y":
            score += points["draw"] + points["Z"]
        else:
            score += points["win"] + points["X"]
print(pts)
print(score)