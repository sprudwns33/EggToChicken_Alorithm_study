N = int(input())
result = 0
while True:
    if not N:
        print(result)
        break
    elif N<0:
        print(-1)
        break
    else:
        if not N%15:
            result += (N//15)*3
            N = 0
        elif not N%5:
            result += (N//5)
            N = 0
        else:
            N -= 3
            result += 1