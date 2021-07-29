X = int(input())

idx = 1
while True:
    if X - idx <= 0:
        break
    X -= idx
    idx += 1

if idx%2 == 1:
    print(f"{idx-X+1}/{X}")
else:
    print(f"{X}/{idx-X+1}")