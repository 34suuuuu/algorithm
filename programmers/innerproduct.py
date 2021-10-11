def solution(a, b):
    res = 0
    plus = list(zip(a, b))
    for i in range(len(plus)):
        res += (plus[i][0]*plus[i][1])
    return res


def solution(a, b):
    res = 0
    for i in range(len(a)):
        res += (a[i] * b[i])
    return res


def solution(a, b):
    return sum([x*y for x, y in zip(a, b)])


a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]

print(solution(a, b))
