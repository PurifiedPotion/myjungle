from collections import deque

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

water = deque()
hedgehog = deque()

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            hedgehog.append((i, j, 0))
            visited[i][j] = True
        elif graph[i][j] == '*':
            water.append((i, j))

def bfs():
    while hedgehog:
        # 먼저 물을 확장
        for _ in range(len(water)):
            x, y = water.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    water.append((nx, ny))

        # 고슴도치 이동
        for _ in range(len(hedgehog)):
            x, y, time = hedgehog.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if graph[nx][ny] == 'D':
                        return time + 1
                    if graph[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        hedgehog.append((nx, ny, time + 1))
    return "KAKTUS"

print(bfs())
