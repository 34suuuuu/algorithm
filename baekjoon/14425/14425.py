# 14425 문자열 집합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = {input().strip() for _ in range(n)}
result = 0
for _ in range(m):
    tmp = input().strip()
    if tmp in s:
        result += 1
print(result)
