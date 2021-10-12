def solution(numbers):
    num = 0
    for i in range(10):
        if i not in numbers:
            num += i
    return num


numbers = [5, 8, 4, 0, 6, 7, 9]
print(solution(numbers))
