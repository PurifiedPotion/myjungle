from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


def bfs(graph, start):
    visited = {node : False for node in graph}
    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


N, M, V = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for node in graph:
    graph[node].sort()


visited = {node : False for node in graph}

dfs = (graph, V, visited)
print()
bfs = (graph, V)
