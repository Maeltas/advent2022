f = open("day3.input")
sum = 0
i = 0
for l in f:
    if i%3==0:
        fp=l.split()[0]
    elif i%3==1:
        sp=l.split()[0]
    elif i%3==2:
        tp=l.split()[0]
        common=[]
        for letter in fp:
            if letter in sp and letter not in common and letter in tp:
                common.append(letter)
        for cm in common:
            if cm == cm.upper():
                sum += ord(cm) - 38
            else:
                sum += ord(cm) - 96
    i += 1
print(sum)
