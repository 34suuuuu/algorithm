def solution(n):
    i = 2
    while i <= n-1:
        if (n-1) % i == 0:
            return i
        else:
            i += 1


print(solution(10))
