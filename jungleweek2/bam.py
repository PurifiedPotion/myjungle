from collections import deque
import sys

N = int(sys.stdin.readline())

graph = [[0]*N for _ in range(N)]

K = int(sys.stdin.readline())

for i in range(K):
    appley, applex = map(int, sys.stdin.readline().split())
    graph[appley-1][applex-1] = 1

L = int(sys.stdin.readline())

move = []

for i in range(L):
    first_input, second_input = sys.stdin.readline().split()
    move.append([int(first_input), second_input])

#R, U, L, D 순
Ymove = [0, -1,  0, 1]
Xmove = [1,  0, -1, 0]
direction = 0

BamCoordinates = deque()
CurrentLocation = [0, 0]
BamCoordinates.append(CurrentLocation[:])
count = 0

while True:
    CurrentLocation[0] += Ymove[direction]
    CurrentLocation[1] += Xmove[direction]
    count += 1

    if (CurrentLocation[0] >= N or CurrentLocation[1] >= N or 
        CurrentLocation[0] < 0 or CurrentLocation[1] < 0 or 
        CurrentLocation[:] in BamCoordinates):
        print(count)
        break

    if graph[CurrentLocation[0]][CurrentLocation[1]] != 1:
        BamCoordinates.popleft()
    else :
        graph[CurrentLocation[0]][CurrentLocation[1]] = 0
    
    BamCoordinates.append(CurrentLocation[:])

    if move and count == move[0][0] :
        if move[0][1] == "L" :
            direction +=1
            direction = direction % 4
            move.pop(0)
        else : 
            direction +=3
            direction = direction%4
            move.pop(0)

