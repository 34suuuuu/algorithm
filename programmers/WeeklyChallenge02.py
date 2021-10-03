def column(matrix, i):
    return [row[i] for row in matrix]


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


def getCount(scores):
    new_list = {}
    for i in scores:
        try:
            new_list[i] += 1
        except:
            new_list[i] = 1
    return new_list


def solution(scores):
    answer = ''
    length = len(scores[0])

    for i in range(length):
        new_list = column(scores, i)
        new_dict = getCount(new_list)

        min = new_list[0]
        max = new_list[0]

        for j in new_list:
            if min > j:
                min = j
            if max < j:
                max = j

        if max == new_list[i] and new_dict[max] == 1:
            del new_list[i]
        elif min == new_list[i] and new_dict[min] == 1:
            del new_list[i]
        avg = getAverage(new_list)
        answer += getGrade(avg)
    return answer
