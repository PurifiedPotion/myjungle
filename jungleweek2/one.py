N = int(input())
circles = []

for _ in range(N):
    x, r = map(int, input().split())
    circles.append((x - r, 1))   # 왼쪽 끝, 여는 괄호
    circles.append((x + r, -1))  # 오른쪽 끝, 닫는 괄호

# 좌표 기준 정렬, 같은 좌표면 닫는 괄호를 먼저 처리
circles.sort(key=lambda x: (x[0], -x[1]))

stack = []
regions = 0

for pos, typ in circles:
    if typ == 1:  # 여는 괄호
        stack.append(pos)
    else:  # 닫는 괄호
        stack.pop()
        regions += 1
        if stack:  # 스택 안에 뭔가 있으면 닫힌 괄호 안에 또 괄호가 있다는 뜻
            regions += 1

print(regions)






