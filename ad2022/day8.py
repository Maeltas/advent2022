f = open("day8.input")
table=[]
for l in f:
    l=l.split()[0]
    table.append(l)
visible=0
for x in range(len(table)):
    for y in range(len(table)):
        if x==0 or y==0 or x==len(table)-1 or y== len(table)-1:
            visible+=1
        else:
            tree_height=table[x][y]
            is_visible=False
            tx=x
            ty=y
            x1=-1
            y1=0
            higher=True
            while(tx>0):
                tx+=x1
                if table[tx][y]>=tree_height:
                    higher=False
                    break
            if tx==0 and higher==True:
                is_visible=True
            if is_visible==False:
                higher=True
                tx = x
                ty = y
                x1 = 1
                y1 = 0
                while (tx < len(table)-1):
                    tx += x1
                    if table[tx][y] >= tree_height:
                        higher = False
                        break
                if tx == len(table)-1 and higher==True:
                    is_visible=True
            if is_visible == False:
                higher = True
                tx = x
                ty = y
                x1 = 0
                y1 = 1
                while (ty < len(table) - 1):
                    ty += y1
                    if table[x][ty] >= tree_height:
                        higher = False
                        break
                if ty == len(table) - 1 and higher==True:
                    is_visible=True
            if is_visible == False:
                higher = True
                tx = x
                ty = y
                x1 = 0
                y1 = -1
                while (ty >0):
                    ty += y1
                    if table[x][ty] >= tree_height:
                        higher = False
                        break
                if ty == 0 and higher==True:
                    is_visible=True
            if is_visible:
                visible+=1

print(visible)
score=[]
for x in range(len(table)):
    for y in range(len(table)):
        if x==0 or y==0 or x==len(table)-1 or y== len(table)-1:
            tree_score=0
        else:
            tree_height=table[x][y]
            tx=x
            ty=y
            x1=-1
            y1=0
            higher=True
            i=0
            while(tx>0):
                i += 1
                tx+=x1
                if table[tx][y]>=tree_height:
                    break
            tree_score=i
            i=0
            tx=x
            while (tx < len(table)-1):
                i += 1
                tx += 1
                if table[tx][y] >= tree_height:
                    break
            tree_score *= i
            i=0
            ty=y
            while (ty > 0):
                i += 1
                ty += -1
                if table[x][ty] >= tree_height:
                    break
            tree_score *= i
            i=0
            ty=y
            while (ty < len(table)-1):
                i += 1
                ty += 1
                if table[x][ty] >= tree_height:
                    break
            tree_score *= i
        score.append(tree_score)
score.sort()
print(score[-1])