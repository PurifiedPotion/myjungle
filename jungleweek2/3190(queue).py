from collections import deque

n = int(input())  # 보드 크기
k = int(input())  # 사과 개수

board = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1  # 사과 위치 표시 (1 기반 → 0 기반)

l = int(input())  # 방향 전환 횟수
directions = {}
for _ in range(l):
    t, d = input().split()
    directions[int(t)] = d

# 방향: 오른쪽, 아래, 왼쪽, 위
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

direction = 0  # 초기 방향: 오른쪽
time = 0
snake = deque()
snake.append((0, 0))  # 시작 위치
visited = set()
visited.add((0, 0))

x, y = 0, 0

while True:
    time += 1
    x += dx[direction]
    y += dy[direction]

    # 벽 또는 자기 몸에 부딪히면 종료
    if not (0 <= x < n and 0 <= y < n) or (x, y) in visited:
        break

    snake.append((x, y))
    visited.add((x, y))

    if board[x][y] == 1:  # 사과가 있으면
        board[x][y] = 0
    else:
        tail = snake.popleft()
        visited.remove(tail)

    if time in directions:
        if directions[time] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

print(time)