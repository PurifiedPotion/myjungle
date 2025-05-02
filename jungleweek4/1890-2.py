n= int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
m = len(graph[0]) 
dp = [[0]*m for _ in range(n)] # 2차원 배열 만들기 위해 n, m 나눔 
dp[0][0] = 1 # 첫번째 칸은 1로 초기화
def solve(): 
    for i in range(n): # 행
        for j in range(n):  # 열
            k = int(graph[i][j]) # 현재 칸 값
            if k == 0 or dp[i][j] == 0 :  #현재 칸이 0 이면 넘어감 
                continue
            if i+k < n: # graph 범위 안에 있으면
                dp[i+k][j] += dp[i][j] # 현재 칸에서 아래로 이동한 칸에 현재 칸의 값을 더함
            if j+k < m:
                dp[i][j+k] += dp[i][j] # 현재 칸에서 오른쪽으로 이동한 칸에 현재 칸의 값을 더함

    return dp[-1][-1]
print(solve())