import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
card = deque()
for _ in range(n):
    card.append(_+1)
while len(card) > 1:
    card.popleft()
    card.append(card.popleft())
print(card.pop())
