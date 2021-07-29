# 백트레킹 풀이
def product(arr, tmp):
    if len(tmp) == length:
        return
    for i in arr:
        tmp += i
        kind.add(tmp)
        product(arr, tmp)
        tmp = tmp[:-1]

N, K = map(int, input().split())
length = len(str(N))
arr = list(map(str, input().split()))

kind = set()
product(arr, '')

kind = list(map(int, kind))
kind.sort()

for i in range(len(kind)-1, -1, -1):
    if kind[i] <= N:
        print(kind[i])
        break

'''
# 라이브러리 사용 풀이
from itertools import product

N, K = map(int,input().split())
arr = list(map(str,input().split()))
length = len(str(N))

kind = []
for i in range(1, length+1):
    tmp = list(map(int, set(map(''.join, product(arr, repeat=i)))))
    for j in tmp:
        kind.append(j)

kind.sort()

for i in range(len(kind)-1, -1, -1):
    if kind[i] <= N:
        print(kind[i])
        break
'''