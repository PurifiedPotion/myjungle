import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

graph = {
    0 : [(1, 6), (2, 7)],
    1 : [(2, 8), (3, 5)],
    2 : [(3, -4), (4, 9)],
    3 : [],
    4 : [(3, 7)]
}

print(dijkstra(graph,0))