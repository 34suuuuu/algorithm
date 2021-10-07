def solution(weights, head2head):
    info = []
    w = len(weights)
    for i in range(w):
        high = [h for h in range(w) if weights[i] < weights[h]]
        fat = 0
        v = 0
        n = 0
        for j in high:
            if head2head[i][j] == "W":
                fat += 1
        for j in range(w):
            if head2head[i][j] == "W":
                v += 1
            elif head2head[i][j] == "N":
                n += 1
            if w == n:
                victory = 0
            else:
                victory = v / (w - n)
        info.append((victory, fat, weights[i], i))
    info = sorted(info, key=lambda x: (x[0], x[1], x[2], -x[3]), reverse=True)
    print(info)
    return [x[3]+1 for x in info]


weights = [50, 82, 75, 120]
head2head = ["NLWL", "WNLL", "LWNW", "WWLN"]
print(solution(weights, head2head))
