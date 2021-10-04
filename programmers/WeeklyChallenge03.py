# def solution(table, languages, preference):
#     answer = ''
#     score = []

#     new_list = []
#     for i in range(len(table[0].split())-1):
#         new_list.append(table[i].split())

#     length = len(new_list)
#     for i in range(length):
#         sum = 0
#         for j in range(len(languages)):
#             if languages[j] in new_list[i]:
#                 sum += ((6 - new_list[i].index(languages[j])) * preference[j])

#         score.append(sum)

#     index = score.index(max(score))
#     answer = new_list[index][0]

#     m = max(score)
#     max_index = [i for i, v in enumerate(score) if v == m]
#     max_list = [new_list[i][0] for i in max_index]
#     max_list.sort()
#     answer = max_list[0]
#     return answer

def solution(table, languages, preference):
    score = {}
    for t in table:
        for lang, pref in zip(languages, preference):
            if lang in t.split():
                score[t.split()[0]] = (6 - t.split().index(lang)) * \
                    pref + score.get(t.split()[0], 0)

    sorted_score = sorted(
        score.items(), key=lambda item: (-item[1], item[0]))
    return sorted_score[0][0]


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
         "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
         "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

print(solution(table, languages, preference))

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

print(solution(table, languages, preference))
