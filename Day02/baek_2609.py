def gcd(a,b):
    if a % b != 0:
        return gcd(b, a%b)
    return b

a, b = map(int, input().split())

gcd_val = gcd(a,b)
lcm_val = a*b//gcd

print(gcd_val)
print(lcm_val)


'''
import math
a,b = map(int, input().split())

print(math.gcd(a,b))
print(a*b//math.gcd(a,b))

def gcd(a,b):
    if a%b != 0:
        return gcd(b,a%b)
    else: return b
'''