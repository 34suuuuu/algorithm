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
left = []
right = []
result = []

for i in range(N):
    num = int(input())

    if len(left) == len(right):  # 짝수일 때
        heapq.heappush(left, (-num, num))
    else:   # 홀수일 떄
        heapq.heappush(right, (num, num))

    if right and left[0][1] > right[0][0]:
        min = heapq.heappop(right)[0]
        max = heapq.heappop(left)[1]
        heapq.heappush(left, (-min, min))
        heapq.heappush(right, (max, max))
    result.append(left[0][1])
for _ in result:
    print(_)
