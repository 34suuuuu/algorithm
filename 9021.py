num = int(input())
for i in range(num):
    command = input()
    stack = []
    for j in range(len(command)):
        if command[j] == '(' or len(stack) == 0:
            stack.append(command[j])
        elif stack[-1] == '(':
            stack.pop()

    if(len(stack) == 0):
        print("YES")
    else:
        print("NO")
