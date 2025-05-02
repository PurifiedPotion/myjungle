import sys

n=int(input())
stklist=[None]*n
ptr=0
size=0
for _ in range(n):
    command = sys.stdin.readline().strip().split()  # 입력을 공백 기준으로 나눔
    if command[0] == "push":
        stklist[ptr] = command[1]
        size+=1
        ptr+=1

    elif command[0] == "pop":
        if ptr>0:
            print(stklist[ptr-1])
            size-=1
            ptr-=1
        else:
            print(-1)
    elif command[0] == "size":
        print(size)
    elif command[0] == "empty":
        if size == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if ptr>0:
            print(stklist[ptr-1])
        else:
            print(-1)
