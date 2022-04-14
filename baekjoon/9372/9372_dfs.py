# 상근이의 여행
from collections import deque
import sys
input = sys.stdin.readline


def dfs(start, cnt):
    visited[start] = True

    for s in graph[start]:
        if not visited[s]:
            cnt = dfs(s, cnt+1)
    return cnt


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    cnt = dfs(1, 0)
    print(cnt)
