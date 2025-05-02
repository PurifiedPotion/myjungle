from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

def find_connected_components_bfs(graph):
    visited = {node: False for node in range(1, N + 1)}
    count = 0

    for node in range(1, N + 1):
        if not visited[node]:
            bfs(graph, node, visited)
            count += 1

    return count

print(find_connected_components_bfs(graph))
