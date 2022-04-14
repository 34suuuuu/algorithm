# 바이러스
import sys
input = sys.stdin.readline


def dfs(start, cnt):
    visited[start] = True

    for s in graph[start]:
        if not visited[s]:
            cnt = dfs(s, cnt+1)
    return cnt


computer = int(input())
link = int(input())
graph = [[]for _ in range(computer+1)]
visited = [False for _ in range(computer+1)]
for c in range(link):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = dfs(1, 0)
print(cnt)
