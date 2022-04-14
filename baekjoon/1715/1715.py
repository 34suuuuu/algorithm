import sys
import heapq
input = sys.stdin.readline

N = int(input())
data = []
for i in range(N):
    heapq.heappush(data, int(input()))

if len(data) == 1:
    print(0)
else:
    result = 0
    while len(data) > 1:
        min1 = heapq.heappop(data)
        min2 = heapq.heappop(data)
        result += (min1 + min2)
        heapq.heappush(data, min1 + min2)
    print(result)
