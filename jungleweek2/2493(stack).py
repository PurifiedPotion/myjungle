N = int(sys.stdin.readline())
top = list(map(int,sys.stdin.readline().split()))
stack = []
ans = [0] * N
for t in range(N) :
    while stack and stack[-1][0] < top[t] :
        stack.pop()
    if stack :
        ans[t] = stack[-1][1]+1
    stack.append([top[t], t])
print(*ans)