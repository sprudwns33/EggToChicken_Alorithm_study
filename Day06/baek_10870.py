def pipo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return pipo(N-1) + pipo(N-2)

N = int(input())
print(pipo(N))