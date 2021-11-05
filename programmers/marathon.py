def solution(participant, completion):
    for i in participant:
        if i in completion:
            continue
        else:
            return i


solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
