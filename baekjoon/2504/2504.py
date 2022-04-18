import sys
input = sys.stdin.readline


def is_checked(command):
    stack = []

    for i in command:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack) == 0:
        return True
    else:
        return False


def calc_value(command):
    stack = []
    value = 0

    for i in command:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                tmp = 0
                for j in range(len(stack)-1, -1, -1):
                    if stack[j] == "[":
                        stack[-1] = tmp * 3
                        break
                    else:
                        tmp += stack[-1]
                        stack.pop()

        elif i == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                tmp = 0
                for j in range(len(stack)-1, -1, -1):
                    if stack[j] == "(":
                        stack[-1] = tmp * 2
                        break
                    else:
                        tmp += stack[-1]
                        stack.pop()
    return sum(stack)


command = input()
if is_checked(command):
    print(calc_value(command))
else:
    print(0)
