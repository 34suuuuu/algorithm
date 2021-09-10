import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    m = int(input())

    if m > 0:
        heapq.heappush(heap, (-m, m))
    elif m == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
