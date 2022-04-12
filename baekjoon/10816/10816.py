# import sys
# input = sys.stdin.readline

# N = int(input())
# getList = list(map(int, input().split()))
# getList.sort()
# M = int(input())
# checkList = list(map(int, input().split()))

# # 중복갯수 미리 확인
# dupList = {}
# for n in getList:
#     if n not in dupList:
#         dupList[n] = 1
#     else:
#         dupList[n] += 1

# for m in checkList:
#     start = 0
#     end = N-1

#     while start <= end:
#         mid = (start + end) // 2
#         if m == getList[mid]:
#             break
#         elif m < getList[mid]:
#             end = mid-1
#         else:
#             start = mid+1
#     if getList[mid] == m:
#         print(dupList[m], end=' ')
#     else:
#         print(0, end=' ')

import sys
input = sys.stdin.readline

N = int(input())
getList = list(map(int, input().split()))
getList.sort()
M = int(input())
checkList = list(map(int, input().split()))


def upperBound(start, end, key):
    while start < end:
        mid = (start + end) // 2
        if getList[mid] <= key:
            start = mid+1
        else:
            end = mid
    return end


def lowerBound(start, end, key):
    while start < end:
        mid = (start + end) // 2
        if getList[mid] < key:
            start = mid + 1
        else:
            end = mid
    return end


result = []
for m in checkList:
    upper = upperBound(0, N, m)
    lower = lowerBound(0, N, m)
    if upper == lower:
        result.append(0)
    else:
        result.append(upper-lower)
for _ in result:
    print(_, end=' ')
