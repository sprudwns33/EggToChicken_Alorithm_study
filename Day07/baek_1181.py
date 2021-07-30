import sys
input = sys.stdin.readline

N = int(input())
arr = set()
for _ in range(N):
    S = input().rstrip()
    arr.add(S)

arr = list(set(arr))
arr.sort(key=lambda x:(len(x),x))
for i in arr:
    print(i)