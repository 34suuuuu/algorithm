import sys
input = sys.stdin.readline

command = input().split()
queue = []
result = []
n = int(command[0])

for i in range(n):
    queue.append(i+1)

k = 1
while(len(queue) != 0):
    if k < 3:
        queue.append(queue.pop())
    elif k == 3:
        result.append(queue.pop())
        k = 1
print(result)
