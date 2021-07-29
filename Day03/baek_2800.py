'''
# 백트레킹 이용
def add_exp(exp, idx, start):
    result.add(''.join(exp))
    for i in range(start, len(idx)):
        if not ck[i]:
            s,e = idx[i]
            exp[s], exp[e] = '(', ')'
            result.add(''.join(exp))
            ck[i] = 1
            add_exp(exp, idx, i+1)
            ck[i] = 0
            exp[s], exp[e] = '', ''

exp = list(map(str, input()))

stack, idx = [], []
result = set()

for i in range(len(exp)):
    if exp[i] == '(':
        stack.append(i)
        exp[i] = ''
    elif exp[i] == ')':
        idx.append((stack.pop(), i))
        exp[i] = ''

ck = [0 for _ in range(len(idx))]

add_exp(exp, idx, 0)

result = list(result)
result.sort()

for i in range(1, len(result)):
    print(result[i])
'''
# 내장함수 combinations이용
from itertools import combinations

exp = list(map(str, input()))
stack, idx = [], []
result = set()

for i in range(len(exp)):
    if exp[i] == '(':
        stack.append(i)
        exp[i] = ''
    elif exp[i] == ')':
        idx.append((stack.pop(), i))
        exp[i] = ''

for i in range(len(idx)):
    comb = list(combinations(idx, i))
    for j in range(len(comb)):
        com = comb[j]
        add_exp = exp[:]
        for k in range(len(com)):
            s,e = com[k]
            add_exp[s], add_exp[e] = '(', ')'
        result.add(''.join(add_exp)) 

result = list(result)
for i in sorted(result):
    print(i)