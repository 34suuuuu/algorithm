import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

d_visited = [False for _ in range(n+1)]


def dfs(v):
    d_visited[v] = True
    print(v, end=' ')
    for g in graph[v]:
        if not d_visited[g]:
            dfs(g)
            d_visited[g] = True


b_visited = [False for _ in range(n+1)]


def bfs(v):
    queue = deque([v])
    b_visited[v] = True

    while queue:
        tmp = queue.popleft()
        print(tmp, end=' ')

        for g in graph[tmp]:
            if not b_visited[g]:
                b_visited[g] = True
                queue.append(g)


dfs(v)
print()
bfs(v)
print()
