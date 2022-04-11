# 2075 N번째 큰 수
# min-heap을 이용해서 우선순위 큐의 길이를 n만큼으로 유지
import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
hq = []

for _ in range(n):
    nums = list(map(int, input().split()))

    if not hq:
        for num in nums:
            heapq.heappush(hq, num)
    else:
        for num in nums:
            if hq[0] < num:
                heapq.heappush(hq, num)
                heapq.heappop(hq)
print(hq[0])
