import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 늘려주기 (안 하면 런타임 에러 남)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
visited = [False] * (N + 1)

# 인접 리스트 구성
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            parent[neighbor] = node  # 현재 노드가 자식의 부모
            dfs(neighbor)

dfs(1)  # 루트는 1번

# 결과 출력 (2번 노드부터)
for i in range(2, N + 1):
    print(parent[i])
