from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

graph = defaultdict(list)

A = list(map(int, input().strip()))

for _ in range(N-1):
    u, v =map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

routes = []

def dfs(graph, v, visited, count, route):

    if A[v-1] == 1 :
        count += 1
    elif A[v-1] == 0 and len(route) == 0:
        return
    
    if count >= 2 :
        route.append(v)
        routes.append(route)
        return
    
    route.append(v)
    
    visited[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, count, route)


for i in range(1, N+1):
    visited = {node: False for node in graph}
    route = []
    dfs(graph, i, visited, 0, route)

print(len(routes))