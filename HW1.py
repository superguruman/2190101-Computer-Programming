# HW01 (Don't delete this line or add any line above this line.)

frames = [float(x) for x in input().split()]

# write your program under this line

def coord(i):
    x,y,w,h=frames[(i-1)*4],frames[(i-1)*4+1],frames[(i-1)*4+2],frames[(i-1)*4+3]
    return x,y,w,h

def center(i):
    x=frames[(i-1)*4]+(frames[(i-1)*4+2]/2)
    y=frames[(i-1)*4+1]-(frames[(i-1)*4+3]/2)
    a=x,y
    return a

def distance(f1,f2):
    f1=center(f1)
    f2=center(f2)
    d=(((float(f2[1])-float(f1[1]))**2)+((float(f2[0])-float(f1[0]))**2))**0.5
    return d

def intersection(f1,f2):
    x1,y1,w1,h1=coord(f1)
    x2,y2,w2,h2=coord(f2)

    #Bottom-Right Coords

    x3=x1+w1
    x4=x2+w2
    y3=y1-h1
    y4=y2-h2

    #Top-Left=Max x, Min y
    #Bot-right=Min x, Max y

    top_left=max(x1,x2), min(y1,y2)
    bot_right=min(x3,x4), max(y3,y4)
    
    area=(top_left[0]-bot_right[0])*(bot_right[1]-top_left[1])
    if area > 0:
        return area
    else:
        return 0.0

def union(f1,f2):
    intersection_area=intersection(f1,f2)
    x1,y1,w1,h1=coord(f1)
    x2,y2,w2,h2=coord(f2)
    area=(w1*h1)+(w2*h2)
    union_area=area-(intersection_area)
    return union_area

def iou(f1,f2):
    inter=intersection(f1,f2)
    uni=union(f1,f2)
    ratio=inter/uni
    return ratio

center_ans=[]
distance_ans=[]
interarea_ans=[]
unionarea_ans=[]
iou_ans=[]

while True:
    a=input().split()
    if a[0] == "end":
        break
    elif a[0] == "center":
        center_ans.append(center(int(a[1])))
    elif a[0] == "distance":
        distance_ans.append(distance(int(a[1]),int(a[2])))
    elif a[0] == "intersection":
        interarea_ans.append(intersection(int(a[1]),int(a[2])))
    elif a[0] == "union":
        unionarea_ans.append(union(int(a[1]),int(a[2])))
    elif a[0] == "iou":
        iou_ans.append(iou(int(a[1]),int(a[2])))
for i in range(len(center_ans)):
    print("("+str(center_ans[i][0])+","+str(center_ans[i][1])+")")
for i in range(len(distance_ans)):
    print(distance_ans[i])
for i in range(len(interarea_ans)):
    print(interarea_ans[i])
for i in range(len(unionarea_ans)):
    print(unionarea_ans[i])
for i in range(len(iou_ans)):
    print(iou_ans[i])