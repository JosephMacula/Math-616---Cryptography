
# Takes a positive integer g, an exponent A, and a modulus N, and computes
# g^A (mod N)

def fast_power_alg(g, A, N):
    b = 1
    while A > 0:
        if A%2 == 1:
            b = (b*g)%N
        g = (g*g)%N
        A = A//2
    return b
