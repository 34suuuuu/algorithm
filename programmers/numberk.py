def solution(array, commands):
    result = []
    for i in range(len(commands)):
        temp = sorted(array[commands[i][0]-1:commands[i][1]])
        result.append(temp[commands[i][2]-1])
    return result
