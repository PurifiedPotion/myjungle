# 세헌이가 푼거
import sys
N = int(sys.stdin.readline())
stack = []
in_s = []
cnt = [N+1]
for i in range(N) :
    a,b = map(int, sys.stdin.readline().split())
    stack.append([a-b,a+b])
stack.sort(key=lambda x: (x[0], -x[1]))
stack.reverse()
print(stack)
def circle_check(x,y) :
    small_circle = []
    for i in range(len(stack)) :
        if  x <= stack[i][0] and y >= stack[i][1] :
            small_circle.append(stack[i])
    sx, sy = x,y
    while small_circle :
        remove_circle = []
        for i in small_circle   :
            if x== i[0] :
                if y== i[1] :
                    cnt[0] += 1
                    return
                else :
                    sx = i[1]
                    remove_circle.append(i)
            else :
                if y== i[1] :
                    sy = i[0]
                    remove_circle.append(i)
        if sy==sx :
            cnt[0] += 1
            return
        if x == sx or y == sy :
            return
        x, y = sx, sy
        for i in remove_circle:
            small_circle.remove(i)
    return
while stack :
    a,b =stack.pop()
    circle_check(a,b)
print(cnt[0])