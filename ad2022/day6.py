f=open("day6.input","r")
i=0
result=14
found=False
for l in f:
    l=l.split()[0]
    while found is False:
        tab=l[i:result]
        print(tab)
        count={}
        for t in tab:
            if t in count.keys():
                count[t]+=1
            else:
                count[t]=1
        unique = True
        for key, val in count.items():
            if val > 1:
                unique = False
        if unique == True:
            break
        i+=1
        result+=1
print(result)
