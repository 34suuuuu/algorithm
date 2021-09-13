import sys
input = sys.stdin.readline

# input().split() -> 띄어쓰기 단위로 리스트에 저장됨
# input() -> 글자 단위로 리스트에 저장됨, 공백도 리스트에 저장됨

while True:
    stack = []
    command = input()
    balance = True
    if command == ".\n":
        break

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
        print("yes")
    else:
        print("no")
