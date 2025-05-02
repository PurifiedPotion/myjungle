import sys

n = int(sys.stdin.readline())
columnlist = [int(sys.stdin.readline()) for _ in range(n)]

i=len(columnlist)-2
highest = columnlist[-1]
count=1

while i >=0:
    if columnlist[i] <= highest:
        i-=1
    else:
        highest = columnlist[i]
        count +=1
        i-=1

print(count)