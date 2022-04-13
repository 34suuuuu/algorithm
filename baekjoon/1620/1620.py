import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pk_name = {}
pk_idx = {}
num = 1

for i in range(N):
    name = input().strip()
    pk_name[num] = name
    pk_idx[name] = num
    num += 1

for _ in range(M):
    pk = input().strip()
    try:
        print(pk_name[int(pk)])
    except:
        print(pk_idx[pk])
