from itertools import permutations

A, B = map(str, input().split())
comb = set(map(''.join, permutations(A, len(A))))
comb = sorted(list(comb))
result = -1

for i in range(len(comb)-1, -1, -1):
    if int(comb[i]) < int(B) and comb[i][0] != '0':
        result = int(comb[i])
        break

print(result)