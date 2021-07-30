import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
tmp = Counter(arr).most_common(2)

print(round(sum(arr)/N))
print(arr[(0+N)//2])
if len(tmp) <= 1:
    print(tmp[0][0])
else: 
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else : print(tmp[0][0])
print(arr[-1]-arr[0])