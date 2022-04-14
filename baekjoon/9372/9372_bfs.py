# 상근이의 여행
from collections import deque
import sys
input = sys.stdin.readline


def bfs(start, cnt):
    queue = deque([start])
    visited[start] = True

    while queue:
        tmp = queue.popleft()
        cnt += 1

        for g in graph[tmp]:
            if not visited[g]:
                visited[g] = True
                queue.append(g)
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
    cnt = bfs(1, -1)
    print(cnt)
