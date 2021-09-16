import sys
input = sys.stdin.readline

n = int(input())
temp = list(map(int, input().split()))
stack = []
for i in temp:
    stack.append(i)

