import math

N = int(input())
repeat = round(math.log(N, 3))

arr = ['***', '* *', '***']
idx = 1
while idx < repeat:
    length = len(arr)
    for i in range(length):
        arr.append(arr[i] + ' '*length + arr[i])

    for i in range(length):
        arr[i] = arr[i]*3
        arr.append(arr[i])
    idx += 1

for i in arr:
    print(i)