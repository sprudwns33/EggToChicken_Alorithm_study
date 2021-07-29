from itertools import combinations

N = int(input())
S = list(map(int, input().split()))
ck = [0 for _ in range(2000001)]

for i in range(N+1):
    combin = list(combinations(S, i))
    for com in combin:
        ck[sum(com)] = 1

for i in range(len(ck)):
    if not ck[i]:
        print(i)
        break

'''
다른사람의 풀이법
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

print(target)
'''