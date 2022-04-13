# push, pop, size,empty, top
import sys
input = sys.stdin.readline

num = int(input())
stack = []
for i in range(num):
    command = input().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif command[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
