N = int(input())
arr = list(map(int, input().split()))
tmp = sorted(list(set(arr)))
result = {}
for i in range(len(tmp)):
    result[tmp[i]] = i

for i in range(N):
    print(result.get(arr[i]), end=" ")