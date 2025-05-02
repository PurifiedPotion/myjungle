
def floyd_warshall(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in graph:
        dist[u][v] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

graph = [
    (0, 1, 3),
    (1, 2, 1),
    (2, 4, 2),
    (4, 3, 4),
    (3, 0, 8)
]

print(floyd_warshall(graph,len(graph)))