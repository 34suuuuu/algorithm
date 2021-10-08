def solution(sizes):
    return max(list(map(max, sizes))) * max(list(map(min, sizes)))


sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))
