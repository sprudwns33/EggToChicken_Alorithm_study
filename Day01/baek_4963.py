import sys
input = sys.stdin.readline

def bfs(maps, a, b):
    ck[a][b] = 1
    q = [(a, b)]

    while q:
        x, y = q.pop()
        for i in range(8):
            xx, yy = x+dx[i], y+dy[i]
            if 0<=xx<h and 0<=yy<w and maps[xx][yy] and not ck[xx][yy]:
                ck[xx][yy] = 1
                q.append((xx, yy))


dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    w, h = map(int, input().split())

    if not w and not h:
        break
    
    maps = [list(map(int, input().split())) for _ in range(h)]
    ck = [[0 for _ in range(w)] for _ in range(h)]

    val = 0
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and not ck[i][j]:
                bfs(maps, i , j)
                val += 1
    print(val)
