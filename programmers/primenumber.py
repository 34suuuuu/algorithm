from itertools import permutations


def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num//2+1):
            if num % i == 0:
                return False
    return True


def solution(numbers):
    result = []
    answer = 0
    for i in range(1, len(numbers)+1):
        result.append(list(set(map(''.join, permutations(numbers, i)))))

    result = list(set(map(int, set(sum(result, [])))))
    for r in result:
        if is_prime(r):
            answer += 1

    return answer


print(solution("17"))
print(solution("011"))
