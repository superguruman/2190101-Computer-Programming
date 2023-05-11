day=int(input())
month=int(input())
year=int(input())-543
m = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 400 == 0:
    m[1]=29
elif year % 4 == 0 and year % 100 != 0:
    m[1]=29
else:
    m[1]=28
smonth=sum(m[0:month-1])
if month == 1:
    print(day)
else:
    print(day+smonth)