import sys

n = int(sys.stdin.readline())

quelist=[]

for i in range(n):
    quelist.append(i+1)

print(quelist)

quelist = [None] * n

print(quelist)