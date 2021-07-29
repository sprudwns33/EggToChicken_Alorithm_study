def bfs(com):
    ck[1] = 1
    q = [1]
    result = 0

    while q:
        val = q.pop()
        for i in range(len(com[val])):
            if not ck[com[val][i]]:
                q.append(com[val][i])
                ck[com[val][i]] = 1
                result += 1
    
    return result

C, N = int(input()), int(input())

com = [[] for _ in range(C+1)]
ck = [0 for _ in range(C+1)]

for _ in range(N):
    a, b = map(int, input().split())
    com[a].append(b)
    com[b].append(a)

print(bfs(com))

'''
예전에 푼 dfs방법
def dfs(x,tmp):
    tmp.append(x)
    ck[x] = 1
    for i in range(len(arr[x])):
        if not ck[arr[x][i]]:
            dfs(arr[x][i],tmp)
    return tmp

C, N = int(input()), int(input())

arr = [[] for _ in range(C+1)]
ck = [0 for _ in range(C+1)]

for _ in range(N):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

print(len(dfs(1,[]))-1)
'''