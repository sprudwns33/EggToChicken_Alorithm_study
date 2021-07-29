from math import sqrt, ceil

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    z = y-x
    val = ceil(sqrt(z)) - 1

    if z <= val**2 + val:
        print(2*val)
    else:
        print(2*val+1)