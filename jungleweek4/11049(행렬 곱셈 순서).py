import sys
input = sys.stdin.readline

N = int(input())

hengryul = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for l in range(2, N+1): # l은 몇 개의 행렬을 곱하는 구간인지 말함, l=2면 (A,B), (B,C), (C,D) l=3이면 (A,B,C), (B,C,D) 그래서 최소가 2
    for i in range(N - l +1): # i 는 구간의 시작 인덱스, j는 끝 인덱스, l을 빼는 이유는 l이 2일때 i는 0,1까지 l이 3일때 i는 0만
        j = i + l -1 # i=0, j=1 이면 (A,B), i=1, j=2면 (B,C) l-1을 더하는 이유는 i의 끝 원소여야 하기 때문
        dp[i][j] = float('inf') # 일단 큰 값으로 초기화
        for k in range(i, j): # k는 괄호를 어디서 칠지 결정하는 분할 지점
            cost = dp[i][k] + dp[k+1][j] + hengryul[i][0] * hengryul[k][1] * hengryul[j][1]
            # dp[i][k]는 i ~ k(왼쪽 덩어리)의 행렬 곱셈 횟수, dp[k+1][j]는 k+1 ~ j(오른쪽 덩어리)의 행렬 곱셈 횟수,
            # hengryul[i][0] * hengryul[k][1] * hengryul[j][1]은 두 덩어리를 합치는 데 드는 곱셈 횟수
            # hengryul[i][0]은 i행렬의 행의 개수, hengryul[k][1]은 k행렬의 열의 개수, hengryul[j][1]은 j행렬의 열의 개수
            dp[i][j] = min(dp[i][j], cost) # 괄호 나누기에 대한 저장

print(dp[0][N-1])