def solution(phone_book):
    phone_book.sort()

    solution1
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True

    solution2
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

    # solution3
    # for p1, p2 in zip(phone_book, phone_book[1:]):
    #     if p2.startswith(p1):
    #         return False
    # return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]	))
