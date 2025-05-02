import sys

def binary_search(thelist, value):
    pl=0
    pr=len(thelist)-1

    while True:
        pc=(pl+pr) // 2
        if thelist[pc] == value:
            return 1
        elif thelist[pc] > value:
            pr = pc-1
        else :
            pl = pc+1

        if pl > pr:
            return 0

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

A.sort()

M = int(sys.stdin.readline())

B = list(map(int, sys.stdin.readline().split()))

for i in B:
    print(binary_search(A, i))