def solution(progresses, speeds):
    result = []
    for p, s in zip(progresses, speeds):
        if len(result) == 0 or result[-1][0] < -((p-100)//s):
            result.append([-((p-100)//s), 1])
        else:
            result[-1][1] += 1
    return [r[1] for r in result]


progresses = [93, 30, 55]
speed = [1, 30, 5]
print(solution(progresses, speed))
