def getGrade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80 and score < 90:
        grade = 'B'
    elif score >= 70 and score < 80:
        grade = 'C'
    elif score >= 50 and score < 70:
        grade = 'D'
    else:
        grade = 'F'
    return grade


def getAverage(scores):
    sum = 0
    for i in scores:
        sum += i

    avg = sum / len(scores)
    return avg


def solution(scores):
    answer = ''
    length = len(scores[0])

    for j in range(length):
        max = scores[0][j]
        min = scores[0][j]

        for i in range(length):
            if max < scores[i][j]:
                max = scores[i][j]
            if min > scores[i][j]:
                min = scores[i][j]

        if max == scores[j][j]:

            del scores[j][j]
            if temp not in scores

        elif min == scores[j][j]:
            del scores[j][j]
        print(max == scores[j][j], min == scores[j][j])

    return scores


scores = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [
    47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]
print(solution(scores))
