import sys

n=int(sys.stdin.readline())
stklist=[None]*n
ptr=0
size=0
for _ in range(n):
    command = int(sys.stdin.readline())
    if command != 0:
        stklist[ptr] = command
        size+=1
        ptr+=1

    elif command == 0:
        if ptr>0:
            size-=1
            ptr-=1
        else:
            print(-1)

print(sum(stklist[0:ptr]))
