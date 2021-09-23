import heapq
import sys
input = sys.stdin.readline

# 시간초과
# N = int(input())
# data = []
# for i in range(N):
#     num = int(input())
#     data.append(num)
#     data.sort()
#     half = len(data) // 2
#     if len(data) % 2 == 0:
#         print(data[half-1])
#     else:
#         print(data[half])


N = int(input())
heap = []]
for i in range(N):
    num = int(input())
    heap.heappush(heap, num)
