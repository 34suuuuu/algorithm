import sys
input = sys.stdin.readline

N = int(input())
getList = sorted(list(map(int, input().split())))
M = int(input())
checkList = sorted(map(int, input().split()))

result = []

for m in checkList:
    start = 0
    end = N-1
    count = 0

    while start <= end:
        mid = (start + end) // 2
        if checkList[m] == getList[mid]:
            count += 1
        elif checkList[m] < getList[mid]:
            end = mid-1
        else:
            start = mid+1

    result.append(count)

print(resut)
