import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listner = set()
observer = set()
for n in range(N):
    listner.add(input())

for m in range(M):
    observer.add(input())

result = list(set(listner & observer))
print(len(result))
for i in result:
    print(i.strip())
