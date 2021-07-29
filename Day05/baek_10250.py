import math
T = int(input())
for _ in range(T):
    H,W,N = map(int, input().split())
    front = N%H
    if not front:
        front = H
    end = math.ceil(N/H)
    print(front*100+end)