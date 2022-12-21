class DirClass:
    def __init__(self,name,parent):
        self.name=name
        self.size=0
        self.children=[]
        self.parent=parent


f=open("day7.input","r")
dirs=[]
cur_dir=""
for l in f:
    l=l[:-1]
    if "cd /" in l:
        dir=DirClass("/",None)
        dirs.append(dir)
        cur_dir=dir
    elif "cd " in l:
        l=l.split(" ")
        if l[2]=="..":
            cur_dir=cur_dir.parent
        else:
            for child in cur_dir.children:
                if child.name==l[2]:
                    cur_dir=child
                    break
    elif " ls" in l:
        pass
    elif "dir " in l:
        dir = DirClass(l.split(" ")[1], cur_dir)
        dirs.append(dir)
        cur_dir.children.append(dir)
    else:
        size=int(l.split(" ")[0])
        tmp_dir=cur_dir
        while tmp_dir!=None:
            tmp_dir.size+=size
            tmp_dir = tmp_dir.parent
sum=0
for d in dirs:
    if d.size<=100000:
        sum+=d.size
print(sum)
answer=[]
sum2=dirs[0].size
free_space=70000000-sum2
print(free_space)
for d in dirs:
    if d.size>=30000000-free_space:
        answer.append(d.size)
print(answer)
answer.sort()
print(answer)
print(answer[0])
