import sys
input = sys.stdin.readline
from collections import deque

def dfs(x,tmp):
    tmp.append(x)
    ck[x] = 1
    for i in graph[x]:
        if not ck[i]:
            dfs(i, tmp)
    return tmp

def bfs(x):
    dq = deque([x])
    ck[x] = 1
    result = []
    while dq:
        val = dq.popleft()
        result.append(val)
        for i in graph[val]:
            if not ck[i]:
                dq.append(i)
                ck[i] = 1
    return result

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1):
    graph[i].sort()

ck = [0 for _ in range(N+1)]
print(*dfs(V,[]))
ck = [0 for _ in range(N+1)]
print(*bfs(V))

'''
def dfs(x, tmp):
    tmp.append(x)
    if x not in graph.keys():
        return tmp
    for i in graph[x]:
        if not i in tmp:
            tmp = dfs(i, tmp)
    return tmp

def bfs(x,tmp):
    tmp.append(x)
    if x not in graph.keys():
        return tmp
    arr = [x]
    while arr:
        for i in graph[arr.pop(0)]:
            if i not in tmp:
                arr.append(i)
                tmp.append(i)
    return tmp



N, M, V = map(int, input().split())
graph = {}
for _ in range(M):
    a,b = map(int, input().split())
    if a in graph:
        graph[a] += [b]
    else: 
        graph[a] = [b]
    if b in graph:
        graph[b] += [a]
    else:
        graph[b] = [a]

for i in graph.keys():
    graph[i].sort()

for i in dfs(V,[]):
    print(i, end=" ")
print()
for i in bfs(V,[]):
    print(i, end=" ")
'''


# def dfs(x):
#     dfs_tmp.append(x)
#     dfs_ck[x] = 1
#     if arr[x]:
#         for i in range(len(arr[x])):
#             if not dfs_ck[arr[x][i]]:
#                 dfs(arr[x][i])
#     return dfs_tmp

# def bfs(x):
#     bfs_tmp = [x]
#     bfs_ck = [0 for _ in range(N+1)]
#     result = []

#     while bfs_tmp:
#         val = bfs_tmp.pop(0)
#         result.append(val)
#         bfs_ck[val] = 1
#         for i in range(len(arr[val])):
#             if not bfs_ck[arr[val][i]]:
#                 bfs_tmp.append(arr[val][i])
#                 bfs_ck[arr[val][i]] = 1
#     return result


# N,M,V = map(int, input().split())

# dfs_tmp = []
# dfs_ck = [0 for _ in range(N+1)]

# arr = [[] for _ in range(N+1)]

# for _ in range(M):
#     A, B = map(int, input().split())
#     arr[A] += [B]
#     arr[B] += [A]

# for i in range(1, N+1):
#     arr[i].sort()
    
# for i in dfs(V):
#     print(i, end=" ")
# print()
# for i in bfs(V):
#     print(i, end=" ")
