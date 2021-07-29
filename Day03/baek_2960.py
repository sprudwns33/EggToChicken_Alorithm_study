N, K = map(int, input().split())

# 지우는 순서를 담을 배열
result = []
# 0 ~ N 까지 result에 담겨있는지 확인하는 배열
arr = [0 for _ in range(N+1)]

for i in range(2, N+1):
    # arr[i]가 1이 아닐 경우 while문을 들어간다.
    if not arr[i]:
        val = i
        idx = 1
        # idx(배수)를 하나씩 늘려주면서 val*idx가 result에 들어가있는지 확인하고
        # result에 없을 시 추가한후 arr[val*idx] = 1 로 바꿔준다.
        while val*idx < N+1:
            if not arr[val*idx]:
                result.append(val*idx)
                arr[val*idx] = 1
            idx += 1

# 배열은 0부터 시작이므로 K-1 => K번째 지워진 수이다.
print(result[K-1])