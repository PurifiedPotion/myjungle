from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, list(input().strip()))) for _ in range(N)]

# 방향 왼 위 오 아래
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

def bfs(y,x):
    queue = deque()
    queue.append((y,x))

    while queue :
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue

            if maze[ny][nx] == 0:
                continue

            if maze[ny][nx] == 1:
                maze[ny][nx] = maze[y][x] + 1
                queue.append((ny,nx))

    return maze[N-1][M-1]

print(bfs(0,0))