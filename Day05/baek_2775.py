T = int(input())
for _ in range(T):
    f, h = int(input()), int(input())
    arr = [[i for i in range(h+1)] for i in range(f+1)]
    if f > 0:
        for i in range(1,f+1):
            for j in range(1,h+1):
                arr[i][j] = sum(arr[i-1][:j+1])
    print(arr[f][h])


# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     k = int(input())
#     n = int(input())

#     people = [i for i in range(n + 1)]

#     for i in range(k):
#         for j in range(1, n + 1):
#             people[j] = people[j] + people[j - 1]

#     print(people[-1])