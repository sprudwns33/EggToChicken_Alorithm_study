import math
A,B,V = map(int,input().split())
val = V-A
up = A-B
print(math.ceil(val/up) + 1)