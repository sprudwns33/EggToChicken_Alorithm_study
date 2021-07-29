N = int(input())
row = list(map(int,input().split()))
row.sort()

for i in range(1, N):
    row[i] += row[i-1]

print(sum(row))