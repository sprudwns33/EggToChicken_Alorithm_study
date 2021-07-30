import sys
input = sys.stdin.readline

N = int(input())

arr = [0 for i in range(10001)]

for i in range(N):
    data = int(input())
    arr[data] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)