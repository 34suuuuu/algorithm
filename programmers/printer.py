import sys
input = sys.stdin.readline


# location은 인덱스와 동일
# 중요도가 같은 경우에는?

def solution(priorities, location):

    result = []
    tuple_priorities = [(i, p) for i, p in enumerate(priorities)]

    while priorities:

        max_num = max(priorities)

        if priorities[0] == max_num:
            result.append(tuple_priorities[0])
            tuple_priorities.pop(0)
            priorities.pop(0)
        else:
            tmp = priorities.pop(0)
            priorities.append(tmp)

            tmp = tuple_priorities.pop(0)
            tuple_priorities.append(tmp)

    for i in range(len(result)):
        if result[i][0] == location:
            return i+1


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1]	, 0))
