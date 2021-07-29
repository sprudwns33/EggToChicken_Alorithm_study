def factor(N):
    if N == 1 or N == 0:
        return 1
    return N * factor(N-1)

N = int(input())
print(factor(N))