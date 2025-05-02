import sys
input = sys.stdin.readline

N, K = map(int, input().split())

materials = [list(map(int, input().split()))for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    w, v = materials[i-1]
    for weight in range(K + 1):
        if weight < w:
            dp[i][weight] = dp[i-1][weight]
        else:
            dp[i][weight] = max(dp[i-1][weight], dp[i-1][weight-w] + v)

print(dp[N][K])