import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 혹시 재귀 깊이 문제 방지

V, E = map(int, input().split())

graph = []

for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append((C, A, B))

graph.sort()

parent = {}

def find(x):
    # 경로 압축 기법 사용
    if parent[x] != x: # parent[원소 값]가 원소와 다르다면
        parent[x] = find(parent[x]) # parent[원소 값] 의 최종 root를 저장한다
    return parent[x] # root 값 반환

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x  # 두 집합을 합침

# 4. 정점 초기화
for edge in graph:
    _, u, v = edge # edges의 _에 가중치, u에 시작점, v에 마지막점 하나씩 저장
    if u not in parent: # u가 parent에 없다면
        parent[u] = u # parent에 u 저장
    if v not in parent: # v가 parent에 없다면
        parent[v] = v # parent에 v 저장

# 5. MST 구성
mst = [] # mst라는 빈 리스트 생성
for weight, u, v in graph: # edges 원소들의 가중치, 처음값, 마지막값 하나씩
    if find(u) != find(v):  # ↑ 사이클 안 생기면, 루트값 비교, 트리 납작하게
        union(u, v) # parent 트리를 납작하게 만듦
        mst.append((u, v, weight)) # 사이클 없는 간선만 mst에 처음값, 마지막값, 가중치 저장

totalsum = 0

for i in range(len(mst)):
    totalsum += mst[i][2]

print(totalsum)