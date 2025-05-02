import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

onefold = 0
zerofold = 0

def lets_count(graph, ystart, xstart, yend, xend):
    global onefold, zerofold

    # 기준값
    base = graph[ystart][xstart]
    same = True

    for i in range(ystart, yend):
        for j in range(xstart, xend):
            if graph[i][j] != base:
                same = False
                break
        if not same:
            break

    # 전부 같은 색이면 카운트
    if same:
        if base == 1:
            onefold += 1
        else:
            zerofold += 1
        return

    # 아니면 4분할
    divide = (yend - ystart) // 2
    count = 0

    while count < 4:
        if count == 0:
            # 왼쪽 위
            lets_count(graph, ystart, xstart, ystart + divide, xstart + divide)
        elif count == 1:
            # 오른쪽 위
            lets_count(graph, ystart, xstart + divide, ystart + divide, xend)
        elif count == 2:
            # 왼쪽 아래
            lets_count(graph, ystart + divide, xstart, yend, xstart + divide)
        elif count == 3:
            # 오른쪽 아래
            lets_count(graph, ystart + divide, xstart + divide, yend, xend)
        count += 1

lets_count(graph, 0, 0, n, n)

print(zerofold)
print(onefold)

