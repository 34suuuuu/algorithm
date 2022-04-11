import sys
input = sys.stdin.readline

stack = []
k = int(input())
for i in range(k):
    num = int(input())
    if(num == 0):
        stack.pop()
    else:
        stack.append(num)

sum = 0
if(len(stack) != 0):
    for i in range(len(stack)):
        sum += stack[i]
print(sum)
