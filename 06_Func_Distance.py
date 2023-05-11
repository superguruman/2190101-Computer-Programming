def distance1(x1, y1, x2, y2):
    d=(((x2-x1)**2)+((y2-y1)**2))**0.5
    return d

def distance2(p1, p2):
    d=p1+p2
    d1=distance1(d[0], d[1], d[2], d[3])
    return d1

def distance3(c1, c2):
    d=distance2(c1[:-1],c2[:-1])
    if d <= c1[-1]+c2[-1]:
        return d, True
    else:
        return d, False

def perimeter(points):
    d=0
    for i in range(len(points)):
        d+=distance2(points[i-1],points[i])
    return d

exec(input().strip())