wordList = []
alphabet = ['A', 'E', 'I', 'O', 'U']


def makeWord(string):
    if len(string) == 6:
        return
    wordList.append(string)
    for i in alphabet:
        makeWord(string + i)


def solution(word):
    for i in alphabet:
        makeWord(i)
    return wordList.index(word) + 1


print(solution("EIO"))
