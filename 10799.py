import sys
input = sys.stdin.readline

stack = []
result = 0
command = input().strip()

for i in range(len(command)):
    if command[i] == '(':
        stack.append(command[i])
    else:
        if command[i-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)
