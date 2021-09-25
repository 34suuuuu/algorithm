import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    num = int(input())

    cloth = dict()
    for j in range(num):
        name, type = input().split()

        if type in cloth.keys():
            cloth[type] += 1
        else:
            cloth[type] = 1

    result = 1
    for key in cloth.keys():
        result *= (cloth[key]) + 1

    print(result - 1)
