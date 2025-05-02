import sys
input = sys.stdin.readline

# 입력
n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

# 결과값 저장 변수
max_result = -sys.maxsize
min_result = sys.maxsize

# 백트래킹 함수
def dfs(index, current_result, plus, minus, mul, div):
    global max_result, min_result

    # 모든 숫자를 다 사용한 경우
    if index == n:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return

    num = nums[index]

    if plus > 0:
        dfs(index + 1, current_result + num, plus - 1, minus, mul, div)
    if minus > 0:
        dfs(index + 1, current_result - num, plus, minus - 1, mul, div)
    if mul > 0:
        dfs(index + 1, current_result * num, plus, minus, mul - 1, div)
    if div > 0:
        # 나눗셈은 양수/음수 나눠서 처리
        if current_result < 0:
            dfs(index + 1, -(-current_result // num), plus, minus, mul, div - 1)
        else:
            dfs(index + 1, current_result // num, plus, minus, mul, div - 1)

# DFS 시작
dfs(1, nums[0], plus, minus, mul, div)

# 출력
print(max_result)
print(min_result)