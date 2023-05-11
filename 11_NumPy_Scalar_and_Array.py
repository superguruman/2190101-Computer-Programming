import numpy as np

def toCelsius(f):
    return (f - 32) * 5 / 9

def BMI(wh):
    w = wh[:,0]
    h = wh[:,1]
    return w/(h/100)**2

def distanceTo(p, Points):
    px = p[0]
    py = p[1]
    x = Points[:,0]
    y = Points[:,1]
    return ((x-px)**2+(y-py)**2)**0.5
    
exec(input().strip())