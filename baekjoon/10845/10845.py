# push, pop, size, empty, front, back

import sys
input = sys.stdin.readline

num = int(input())
queue = []

for i in range(num):
    command = input().split()
    if command[0] == "push":
        queue.insert(0, command[1])
    elif command[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if(len(queue) == 0):
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[-1])
    elif command[0] == "back":
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[0])
