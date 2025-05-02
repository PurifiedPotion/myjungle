from collections import deque
import sys
input = sys.stdin.readline

def is_bipartite(start):
    queue = deque([start])
    color[start] = 1  # 시작 정점은 색 1로 칠함
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if color[neighbor] == 0:  # 아직 색칠 안됨
                color[neighbor] = -color[node]  # 반대 색으로 칠함
                queue.append(neighbor)
            elif color[neighbor] == color[node]:  # 인접 노드가 같은 색이면 이분 그래프 아님
                return False
    return True

K = int(input())  # 테스트 케이스 개수
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    color = [0] * (V + 1)
    
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    is_possible = True
    for i in range(1, V + 1):
        if color[i] == 0:
            if not is_bipartite(i):
                is_possible = False
                break
    
    print("YES" if is_possible else "NO")
