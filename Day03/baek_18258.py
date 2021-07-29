import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque()

for i in range(N):
    string = input().split()
    if string[0] == 'push':
        queue.append(string[1])
    elif string[0] == 'pop':
        print(queue.popleft()) if queue else print(-1)
    elif string[0] == 'size':
        print(len(queue))
    elif string[0] == 'empty':
        print(1) if not queue else print(0)
    elif string[0] == 'front':
        print(queue[0]) if queue else print(-1)
    else:
        print(queue[-1]) if queue else print(-1)