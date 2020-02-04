# A function for adding elements of a given elliptic curve
from inverse_from_gcd import inverse_from_gcd



def elliptic_mod_add(p1, p2, q1, q2, a, b, m):
    if p1 == "O" and p2 == "O":
        return q1, q2
    if q1 == "O" and q2 == "O":
        return p1, p2
    if p1 == q1 and p2 == -q2:
        return "O", "O"
    if p1 == q1 and p2 == q2:
        r = (3*(p1**2) + a)*inverse_from_gcd((2*p2), m) % m
    if p1 != q1 or p2 != q2:
        r = (1*(q2-p2))*inverse_from_gcd((q1-p1), m) % m
    x = ((r**2) - p1 - q1) % m
    y = (r*(p1-x)-p2) % m
    return x, y

