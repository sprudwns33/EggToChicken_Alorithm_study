import math

N = int(input())
top = list(map(int, input().split()))
stack = [(math.inf, 0)]
idx = 1
result = []

for i in range(N):
    if top[i] < stack[-1][0]:
        result.append(stack[-1][1])
        stack.append((top[i], idx))
    else:
        while True:
            stack.pop()
            if top[i] < stack[-1][0]:
                result.append(stack[-1][1])
                stack.append((top[i], idx))
                break
    idx += 1

print(*result)
'''
import heapq
import math

N = int(input())
top = list(map(int, input().split()))
tmp = [(math.inf, 0)]
idx = 1
result = []

for i in range(N):
    if top[i] < tmp[0][0]:
        result.append(tmp[0][1])
        heapq.heappush(tmp, (top[i], idx))
    else:
        while True:
            heapq.heappop(tmp)
            if top[i] < tmp[0][0]:
                result.append(tmp[0][1])
                heapq.heappush(tmp, (top[i], idx))
                break
    idx += 1

print(*result)
'''