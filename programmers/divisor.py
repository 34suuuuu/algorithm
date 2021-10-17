# def solution(left, right):
#     return sum(i * (-1 if int(i**0.5) == i**0.5 else 1) for i in range(left, right+1))

def solution(left, right):
    sum = 0
    for i in range(left, right+1):
        tmp = i**0.5
        if tmp == int(tmp):
            sum -= i
        else:
            sum += i
    return sum


print(solution(13, 17))
