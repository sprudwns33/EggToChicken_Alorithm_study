N = int(input())

# 가장 작은 값인 123 부터 987 까지 0을 포함하지 않고 각자리수가 서로 다른 숫자만 리스트에 저장
num_list = [str(i) for i in range(123,988) if '0' not in str(i) and (str(i)[0] != str(i)[1] and str(i)[1] != str(i)[2] and str(i)[0] != str(i)[2])]

for _ in range(N):
    num, s, b = map(int, input().split())
    # 한 줄이 실행될때마다 포함되는 숫자를 저장할 배열
    new_num_list = []
    for num_ck in num_list:
        s_ck = 0
        b_ck = 0
        # 백의자리, 십의자리, 일의자리 순서대로 input값의 num에 포함이 되면 if문 통과
        for j in range(3):
            if num_ck[j] in str(num):
                # num의 자리와 num_ck의 자리수가 동일하면 s_ck를 올리고 아니면 b_ck를 올린다.
                if num_ck[j] == str(num)[j]:
                    s_ck += 1
                else:
                    b_ck += 1
        if s_ck == s and b_ck == b:
            new_num_list.append(num_ck)
    num_list = new_num_list

print(len(num_list))
