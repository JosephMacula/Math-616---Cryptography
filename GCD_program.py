#Calculates the greatest common divisor of two integers, a and b

def gcd_calc(a, b):
    u = 1
    g = a
    x = 0
    y = b
    if b == 0:
        return str(int(a))+' and '+str(int(b))+' have no greatest common divisor'
    while y != 0:
        t = g%y 
        q = g // y
        s = u - q*x
        u = x
        g = y
        x = s
        y = t
    if y == 0:
        v = (g-a*u)/b
        if u < 0:
            while u < 0:
                u = u + b/g
                v = v - a/g
            return int(g)
        
        return int(g)