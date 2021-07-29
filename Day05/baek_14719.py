H, W = map(int, input().split())
block = list(map(int, input().split()))

result = 0
for i in range(1, len(block)-1):
    max_val = block[i-1]
    if block[i] >= max_val:
        continue
    tmp = 0
    for j in range(i+1, len(block)):
        if block[i] < block[j]:
            tmp = max(block[j], tmp)
            if tmp >= max_val:
                tmp = max_val
                break
    if tmp:
        result += tmp-block[i]
        block[i] = tmp

print(result)