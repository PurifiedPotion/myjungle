import heapq
import sys
input = sys.stdin.readline

n = int(input())
maze = [list(map(int, input().strip())) for _ in range(n)]

# 왼 위 오 아
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

def dijkstra():
    # 시작은 (0,0)에서 시작, 바꾼 방 수는 0
    heap = [(0, 0, 0)]
    visited = [[False]*n for _ in range(n)]
    dist = [[float('inf')]*n for _ in range(n)]
    dist[0][0] = 0

    while heap:
        cost, y, x = heapq.heappop(heap)
        if visited[y][x]:
            continue
        visited[y][x] = True

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= nx < n and 0 <= ny < n:
                # 현재까지의 비용 + (검은 방이면 1, 흰 방이면 0)
                next_cost = cost + (1 if maze[ny][nx] == 0 else 0)

                if next_cost < dist[ny][nx]:
                    dist[ny][nx] = next_cost
                    heapq.heappush(heap, (next_cost, ny, nx))

    return dist[n-1][n-1]

print(dijkstra())
