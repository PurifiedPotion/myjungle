from collections import deque
import sys

input = sys.stdin.readline  # 빠른 입력

# 상자 크기
M, N, H = map(int, input().split())

# 3차원 리스트 (z, y, x)
tomato = [[[0] * M for _ in range(N)] for _ in range(H)]

# 입력 받기
for h in range(H):
    for n in range(N):
        tomato[h][n] = list(map(int, input().split()))

# 이동 방향 (6방향): 상하좌우 + 위아래
dz = [0, 0, 0, 0, 1, -1]  # 높이(z)
dy = [-1, 1, 0, 0, 0, 0]  # 세로(y)
dx = [0, 0, -1, 1, 0, 0]  # 가로(x)

# BFS 준비
queue = deque()

# 익은 토마토(1) 위치를 큐에 미리 넣음
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[z][y][x] == 1:
                queue.append((z, y, x))

# BFS 실행
while queue:
    z, y, x = queue.popleft()

    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]

        # 범위 체크
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = tomato[z][y][x] + 1
                queue.append((nz, ny, nx))

# 결과 계산
result = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[z][y][x] == 0:
                print(-1)
                exit()
            result = max(result, tomato[z][y][x])

# 처음에 익은 토마토는 1이므로 -1 해줌
print(result - 1)
