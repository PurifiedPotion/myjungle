from collections import defaultdict
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = defaultdict(list)

for i in range(1, N + 1):
    graph[i] = []

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append((v, 1))

import heapq

def dijkstra(graph, start): # 처음에 그래프와 시작하는 정점을 받는다
    distances = {node: float('inf') for node in graph} # distances라는 딕셔너리를 만들고 각 노드들에 무한대 값을 넣는다
    distances[start] = 0 # 시작하는 정점의 값은 무한대에서 0으로 바뀐다
    queue = [(0, start)] # 큐에 0과 start 튜플을 넣는다

    while queue: # 큐에 원소가 있으면
        current_dist, current_node = heapq.heappop(queue) # 큐에서 낮은 원소 팝한것을 current_dist, current_node에 저장한다. 처음 current_dist는 0

        if current_dist > distances[current_node]: # current_dist 가 distances[start 노드] 라면, 처음에는 같음. while 아래 for문 진행X
            continue                               # 해당 조건문이 있는 이유는 current_dist가 이미 더 크다면 최솟값을 구할 이유X

        for neighbor, weight in graph[current_node]: # 현재 노드값의 모든 이웃과, 가중치중 하나씩
            distance = current_dist + weight # distance는 current_dist + 가중치로 저장
            if distance < distances[neighbor]: # distance가 처음에는 무한대보다 작게된다
                distances[neighbor] = distance # 무한대값이 current_dist + 가중치로 update
                heapq.heappush(queue, (distance, neighbor)) # queue에 (distance,이웃) 튜플 push

    return distances

shortest_distances = dijkstra(graph, X)

count = 0

result = [node for node, dist in shortest_distances.items() if dist == K]

if result:
    result.sort()
    for r in result:
        print(r)

else:
    print(-1)