# def solution(n):
#     mod_list = []
#     res = 0
#     while n:
#         mod = n % 3
#         n = n//3
#         mod_list.append(mod)

#     for i in range(len(mod_list)):
#         res += (mod_list[i] * pow(3, len(mod_list) - i-1))
#     return res

# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n//3
#     res = int(tmp, 3)
#     return res


# n = 125
# print(solution(n))

print(int('100', 2))
print(int('200', 3))
print(int('300', 4))
print(int('400', 5))
print(int('500', 6))
print(int('1000', 16))
