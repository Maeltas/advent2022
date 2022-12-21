f=open("day1.input","r")
most=0
actual=0
calories=[]
for l in f:
    if l!="\n":
        l=l.split()[0]
        actual+=int(l)
    else:
        if actual>most:
            most=actual
        calories.append(actual)
        actual=0
print(most)
calories.sort(reverse=True)
print(calories[0]+calories[1]+calories[2])