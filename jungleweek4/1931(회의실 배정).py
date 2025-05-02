from sys import stdin

input = stdin.readline

N = int(input())
discussion = [list(map(int, input().split())) for _ in range(N)]

discussion.sort(key=lambda x: (x[1], x[0]))

end_time = discussion[0][1]
count = 1

for i in range(1, N):
    if discussion[i][0] >= end_time:
        count += 1
        end_time = discussion[i][1]

print(count)
