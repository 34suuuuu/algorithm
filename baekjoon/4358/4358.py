import sys
import heapq
input = sys.stdin.readline

cnt = 0
species = {}

while True:
    tree = input().rstrip()
    if not tree:
        break
    else:
        if tree in species:
            species[tree] += 1
        else:
            species[tree] = 1
        cnt += 1

species = sorted(species.items())
for name, num in species:
    print("%s %.4f" % (name, num/cnt*100))
