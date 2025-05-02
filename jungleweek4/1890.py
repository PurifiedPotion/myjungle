# 시간 초과

import sys
input = sys.stdin.readline

N = int(input())

jump = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 1]
dx = [1, 0]

count=0

def jumping(y, x):
    global count
    mult = jump[y][x]

    for i in range(2):
        ny, nx = y + dy[i]*mult, x + dx[i]*mult
        if 0<=ny<N and 0<=nx<N:
            if jump[ny][nx] == 0:
                count += 1
                continue
            else :
                jumping(ny,nx)
        else :
            continue

jumping(0,0)
print(count)