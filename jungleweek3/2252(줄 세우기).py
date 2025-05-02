from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)

for i in range(1, N + 1):
    graph[i] = []

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append((v))

def topological_sort(graph):
    indegree = {node: 0 for node in graph} # indegree 에 모든 노드에 0 저장
    for u in graph: # 그래프의 모든 노드 하나씩
        for v in graph[u]: # 노드 하나의 이웃
            indegree[v] += 1 # indegree[이웃]에 1 증가, 최종적으로는 C와 F가 값이 많다
                                                                   # 아래는 진입 차수(in-degree) == 0 분류
    queue = deque([node for node in graph if indegree[node] == 0]) # queue라는 데크에 indegree[node] == 0  
    result = [] # 리스트 생성                                        # 인 것들을 추가 (A,B)

    while queue: # 큐에 노드가 있다면
        node = queue.popleft() # 큐에서 첫번째 원소를 팝한것을 노드에 저장, queue -1
        result.append(node) # result에 노드 추가

        for neighbor in graph[node]: # 노드의 이웃들중 하나씩
            indegree[neighbor] -= 1 # 이웃의 indegree를 1 감소
            if indegree[neighbor] == 0: # 여기서 이웃의 indegree가 0이 되면
                queue.append(neighbor) # 다시 큐에 추가

    # 사이클이 있을 경우 예외 처리
    if len(result) != len(graph): # 사이클이 있으면 만족 하지 않음
        return "사이클 있음! 위상 정렬 불가"
    return result # result 값 출력

print(*topological_sort(graph))