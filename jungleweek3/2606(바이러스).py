from collections import defaultdict, deque
import sys
input = sys.stdin.readline

Computer = int(input())
edges = int(input())
graph = defaultdict(list)

for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, start, visited, component):
    queue = deque([start]) # start(노드)를 queue에 추가
    visited[start] = True # start(노드) 방명록 서명

    while queue: # 큐가 있다면
        v = queue.popleft() # 디큐해서 v로 저장 여기서는 start(노드)
        component.append(v) # 리스트에 start(노드) 추가
        for neighbor in graph[v]: # start(노드)의 모든 이웃중 한명씩
            if not visited[neighbor]: # 방문 안했다면
                visited[neighbor] = True # 방문 서명하고
                queue.append(neighbor) # 리스트에 추가

def find_connected_components_bfs(graph):
    visited = {node: False for node in graph} # 먼저 방명록 초기화
    components = [] # 연결 요소용 리스트

    for node in graph: # 그래프의 모든 노드 하나씩
        if not visited[node]: # 방문 안했다면
            component = [] # 리스트 초기화
            bfs(graph, node, visited, component) # graph, 노드, 방명록, 리스트 송부
            components.append(component) # 이웃끼리의 리스트 추가

    return components

muggeum = find_connected_components_bfs(graph)

count = 0

for i in muggeum:
    if 1 in i:
        print(len(i)-1)
    else :
        count += 1

if count == len(muggeum):
    print(0)