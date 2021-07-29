from collections import deque

N = int(input())

# 1부터 N까지 덱을 생성
card_dq = deque([i for i in range(1, N+1)])
# 덱의 길이가 1이 될 때까지 반복
# 맨앞의 원소를 제거 후, 그 다음 오는 맨앞의 원소를 뒤로 이동 작업 반복
while len(card_dq) > 1:
    card_dq.popleft()
    card_dq.append(card_dq.popleft())

print(card_dq[0])