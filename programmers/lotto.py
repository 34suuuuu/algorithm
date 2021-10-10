# 해시 이용
# def solution(lottos, win_nums):
#     rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
#     return rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]

def solution(lottos, win_nums):

    set_lottos = set(lottos)
    win_nums = set(win_nums)

    tmp = len(set_lottos & win_nums)
    if tmp < 2:
        if lottos.count(0) + tmp < 2:
            return [6, 6]
        else:
            return sorted([6,  7-(len(set_lottos & win_nums) + lottos.count(0))])

    else:
        return sorted([7 - tmp,  7-(len(
            set_lottos & win_nums) + lottos.count(0))])


lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
print(solution(lottos, win_nums))
