import sys
input = sys.stdin.readline

# 방법1. 재귀를 이용한 방법


def solution(numbers, target):

    answer = 0
    length = len(numbers)

    def dfs(idx, result):
        if idx == length:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result-numbers[idx])
            dfs(idx+1, result+numbers[idx])
        return answer
    return dfs(0, 0)


# 방법2. 단순 연산 이용
# def solution(numbers, target):
#     sup = [0]
#     for i in numbers:
#         sub = []
#         for j in sup:
#             sub.append(j+i)
#             sub.append(j-i)
#         sup = sub
#     return sup.count(target)


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
