import sys
from itertools import combinations

n, k = map(int,sys.stdin.readline().split())
heights = list(sys.stdin.readline().strip())


print(n,k)
print(heights)

comb_list = list(combinations(heights, n-k))

for i in range(len(comb_list)):
    for j in range(len(comb_list[i])):
        sumlist = []
        sumlist.append(comb_list[i][j])