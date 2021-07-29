import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    # input값을 val로 저장
    val = int(input())
    # val이 0이 아니면 내장 라이브러리 heap을 통해 절댓값으로 추가
    if val:
        heapq.heappush(arr, (abs(val), val))
    # val이 0일때 배열이 비어있으면 0을 출력, 아니면 heap의 맨앞의 원소를 출력
    else:
        print(heapq.heappop(arr)[1]) if arr else print(0)



'''
예전에 푼 풀이
import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    if not x:
        if arr:
            a,b = heapq.heappop(arr)
            print(b)
        else: print(0)
    else:
        heapq.heappush(arr, (abs(x),x))
'''