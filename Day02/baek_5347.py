import sys
input = sys.stdin.readline

def gcd(a,b):
    if a % b != 0:
        return gcd(b, a%b)
    return b

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    gcd_val = gcd(a,b)
    print(a*b//gcd_val)