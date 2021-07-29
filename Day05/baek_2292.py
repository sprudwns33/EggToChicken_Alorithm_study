N = int(input())-1
count = 1
val = 1
while N>0:
    N = N-6*val
    val += 1
    count += 1
print(count)