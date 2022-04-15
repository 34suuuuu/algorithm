import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
# 파이썬이 정한 최대 깊이보다 더 깊은 재귀가 발생할 때 문제 발생
# 1. 재귀의 깊이를 설정할 수 있는 최대값으로 지정
# 2. 재귀를 사용하지 않는 방향으로


def getParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]


def unionParent(parent, x, y):
    a = getParent(parent, x)
    b = getParent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 0:
        unionParent(parent, a, b)
    else:
        if getParent(parent, a) == getParent(parent, b):
            print("YES")
        else:
            print("NO")
