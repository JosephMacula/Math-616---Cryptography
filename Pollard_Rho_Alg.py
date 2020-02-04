from GCD_program import gcd_calc
from Extended_Euclidean_Algorithm import extended_gcd_calc
from Fast_power_alg import fast_power_alg

#pollard_func is used to calculate x sub i and y sub i, referred to as a and b,
#respectively.

def pollard_func(a, g, h, p):
    if a < p/3:
        a = (g*a)%p
        return a
    elif a >= p/3 and a < (2*p)/3:
        a = (a**2)%p
        return a
    else:
        a = (h*a)%p
        return a

#the values p, g, and h are the prime modulus, the given primitive root of
#F sub p, and the value to which g**t is congruent mod p, respectively.
        
p = 15239131
h = 5953042
g = 29

#Here I initialize a and b, and then compute a sub 2 and b sub 2. That way, I
#can run a while loop to find the next index i and which a sub i is congruent mod
#p to b sub i.

a = 1
b = 1
a = pollard_func(a, g, h, p)
b = pollard_func(pollard_func(b, g, h, p), g, h, p)

#This while loop determines the index i for which a sub i is congruent mod p 
#to b sub 2*i, as well as the values of a sub i and b sub i.

i = 1
while a != b:
    a = pollard_func(a, g, h, p)
    b = pollard_func(pollard_func(b, g, h, p), g, h, p)
    i += 1

#The following while loops calculate alpha, beta, gamma, and delta at the index
# value i
    
a = 1
alpha = 0
beta = 0

j = 0
while j < i:
    if a < p/3:
        a = (g*a)%p           
        alpha = (alpha + 1)%(p-1)
        beta = beta%(p-1)
        j += 1
    elif a >= p/3 and a < (2*p)/3:
        a = (a**2)%p
        alpha = (2*alpha)%(p-1)
        beta = (2*beta)%(p-1)
        j += 1
    else:
        a = (h*a)%p
        alpha = alpha%(p-1)
        beta = (beta + 1)%(p-1)
        j += 1

b = 1
gamma = 0
delta = 0
k = 0
while k < i:
    if b < p/3:
        b = (g*b)%p
        gamma = (gamma + 1)%(p-1)
        delta = delta%(p-1)
        k += .5
    elif b >= p/3 and b < (2*p)/3:
        b = (b**2)%p
        gamma = (2*gamma)%(p-1)
        delta = (2*delta)%(p-1)
        k += .5
    else:
        b = (h*b)%p
        gamma = gamma%(p-1)
        delta = (delta + 1)%(p-1)
        k += .5    

#The following variables are the ones we need to compute the possible values
#of the discrete log.
        
u = (alpha - gamma)%(p-1)
v = (delta - beta)%(p-1)
d = gcd_calc(v, p-1)
s = extended_gcd_calc(v, p-1)[1]
w = (s*u)%(p-1)
z = (p-1)/d

#This while loop calculates the possible values of the discrete log and puts 
#them in an array

x = [w/d]
k = 1
while k < d:
    x.append(w/d + k*z)
    k += 1

#This loop iterates over the array created above and spits out the discrete log
for i in range(0, len(x)):
    if fast_power_alg(g, x[i], p) == h:
        print(int(x[i]))
        break
