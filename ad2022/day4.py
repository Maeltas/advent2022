sum=0
sum2=0
f=open("day4.input")
for l in f:
    l=l.split()[0]
    l= l.split(",")
    first=l[0].split("-")
    second=l[1].split("-")
    f_1=int(first[0])
    f_2=int(first[1])
    s_1=int(second[0])
    s_2=int(second[1])
    if f_1>=s_1 and f_2<=s_2:
        sum+=1
    elif s_1>=f_1 and s_2<=f_2:
        sum+=1

    if f_1>=s_1 and s_2>=f_1:
        sum2+=1
    elif f_2>=s_1 and s_2>=f_2:
        sum2+=1
    elif s_1>=f_1 and f_2>=s_1:
        sum2+=1
    elif s_2>=f_1 and f_2>=s_2:
        sum2+=1

print(sum)
print(sum2)
