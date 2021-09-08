import sys
input = sys.stdin.readline


def binary(a, x):
    start = 0
    end = len(a)-1
    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1


N = int(input())
getList = sorted(list(map(int, input().split())))
M = int(input())
checkList = sorted(map(int, input().split()))

result = {}
for n in getList:
    if n not in result:
        result[n] = 1
    else:
        result[n] += 1

for m in checkList:
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if m == getList[mid]:
            break
        elif m < getList[mid]:
            end = mid-1
        else:
            start = mid+1
    if getList[mid] == m:
        print(result[m], end=' ')
    else:
        print(0, end=' ')
