from collections import defaultdict, deque

N = int(input())  # 부품 수
M = int(input())  # 조립 규칙 수

# 그래프 구성
graph = defaultdict(list)
indegree = [0] * (N + 1)

# 각 부품을 만들기 위해 필요한 기본 부품 수 저장 배열
# needs[x][y] = x번 부품을 만들기 위해 y번 기본 부품이 몇 개 필요한가
needs = [[0] * (N + 1) for _ in range(N + 1)]

# 입력 받기
for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append((X, K))  # Y를 사용해 X를 K개 만든다
    indegree[X] += 1         # X는 Y에 의존

# 기본 부품 여부 판별
is_basic = [False] * (N + 1)
queue = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        is_basic[i] = True
        queue.append(i)

# 위상 정렬 시작
while queue:
    now = queue.popleft()
    for next_part, count in graph[now]:
        if is_basic[now]:  # 기본 부품이면
            needs[next_part][now] += count
        else:
            for i in range(1, N + 1):
                needs[next_part][i] += needs[now][i] * count

        indegree[next_part] -= 1
        if indegree[next_part] == 0:
            queue.append(next_part)

# 완성품(N번)을 만들기 위해 필요한 기본 부품만 출력
for i in range(1, N + 1):
    if is_basic[i] and needs[N][i] > 0:
        print(i, needs[N][i])