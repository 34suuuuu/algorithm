def solution(absolutes, signs):
    return sum(absolutes[i] * (1 if signs[i] else -1) for i in range(len(signs)))


absolutes = [4, 7, 12]

signs = [True, False, True]
print(solution(absolutes, signs))
# print(signs)
