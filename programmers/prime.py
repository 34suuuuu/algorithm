from itertools import combinations


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(nums):
    res = 0
    num_list = list(combinations(nums, 3))
    for num in num_list:
        sum_num = sum(num)
        if is_prime(sum_num):
            res += 1

    return res


nums = [1, 2, 4, 3]
print(solution(nums))
