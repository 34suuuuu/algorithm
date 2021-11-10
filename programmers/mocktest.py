def solution(answers):
    answer = []
    result = [0] * 3

    for i, ans in enumerate(answers):
        tmp1 = i % 5 + 1
        if ans == tmp1:
            result[0] += 1

        list2 = [2, 1, 2, 3, 2, 4, 2, 5]
        tmp2 = i % 8
        if ans == list2[tmp2]:
            result[1] += 1

        list3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        tmp3 = i % 10
        if ans == list3[tmp3]:
            result[2] += 1

    for person, score in enumerate(result):
        if score == max(result):
            answer.append(person + 1)

    return answer


answer = [1, 3, 2, 4, 2]
print(solution(answer))
