import sys
input = sys.stdin.readline

command = input()
res = ' '
stack = []

for i in command:
    if i.isalpha():
        res += i
    else:
        if i == '(':
            stack.append(i)

        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(i)

        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(i)

        elif i == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()

print(res)
