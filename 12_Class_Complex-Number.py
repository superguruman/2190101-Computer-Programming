class Complex:
    def __init__(self,a,b):
        self.r = a
        self.i = b
        
    def __str__(self):
        if self.r == 0:
            if self.i == 0:
                return '0'
            if self.i == 1:
                return 'i'
            if self.i == -1:
                return '-i'
            return str(self.i)+'i'
        if self.i == 0:
            return str(self.r)
        if self.i < 0:
            if self.i == -1:
                return str(self.r)+'-i'
            return str(self.r)+str(self.i)+'i'
        if self.i == 1:
            return str(self.r)+'+i'     
        return str(self.r)+'+'+str(self.i)+'i'
    
    def __add__(self, rhs):
        self.r+=rhs.r
        self.i+=rhs.i
        return self
          
    def __mul__(self, rhs):
        a = (self.r*rhs.r) - (rhs.i*self.i)
        self.i = (self.r*rhs.i) + (self.i*rhs.r)
        self.r = a
        return self
    
    def __truediv__(self, rhs):
        a = ((self.r*rhs.r) + (self.i*rhs.i))/((rhs.r**2)+(rhs.i**2))
        b = (-(self.r*rhs.i)+(self.i*rhs.r))/((rhs.r**2)+(rhs.i**2))
        self.r = a
        self.i = b
        return self
    
t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else: print(c1/c2)