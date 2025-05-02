from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 혹시 재귀 깊이 문제 방지

N, M, V = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)  # 양방향 추가

for node in graph:
    graph[node].sort()  # 방문 순서 오름차순 정렬

def dfs(graph, v, visited): 
    visited[v] = True # 방문한 위치 False → True로 값 변경
    print(v, end=' ')  # 방문 노드 출력

    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited) # 재귀 함수

visited = {i: False for i in range(1, N+1)}

dfs(graph, V, visited)  # V부터 탐색 시작

def bfs(graph, start):
    visited = {node: False for node in graph} # visited 딕셔너리에 graph의 모든 노드 받아와서 node:False 저장
    queue = deque([start]) # start를 deque로 변환
    visited[start] = True # visited[start] == False 였는데, True로 변환

    while queue: # queue에 원소가 있을때
        v = queue.popleft() # queue의 앞 원소 출력, 그것이 v가 됨
        print(v, end=' ')  # 방문 노드 출력

        for neighbor in graph[v]: # graph[0] 안에는 [2,3] 존재
            if not visited[neighbor]: # visited[2] 가 이웃(같은 레벨)이고 False라면,
                queue.append(neighbor) # 큐에 2를 넣는다
                visited[neighbor] = True # visited[2]의 값을 True로 변경

print()
bfs(graph, V)