# 1874 스택 수열
from collections import deque
import sys
input = sys.stdin.readline

num = int(input())
result = []
op = []
flag = True
n = 1

for i in range(num):
    command = int(input())

    while n <= command:
        result.append(n)
        op.append('+')
        n += 1
    if result[-1] == command:
        result.pop()
        op.append('-')
    else:
        flag = False
if flag:
    for i in op:
        print(i)
else:
    print('NO')

# 1부터 입력받은 수까지를 살피는 방법
# 원하는 순서의 숫자와 1부터 증가하는 숫자를 비교해서 작으면 리스트에 push하고 op에  +
# 같아지면 pop, op에 -
# 이러한 과정이 끝나고 전부 pop을 했을 때 순서대로 되지 않으면 NO
# 된다면 op 한 줄씩 출력
