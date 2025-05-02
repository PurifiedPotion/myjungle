import sys

n = int(sys.stdin.readline())

quelist=[None]*n
front = rear = 0
number = 0

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        quelist[rear] = command[1]
        rear += 1
        number += 1
    elif command[0] == "pop":
        if number >0:
            print(quelist[front])
            front += 1
            number -= 1
        else :
            print(-1)
    elif command[0] == "size":
        print(number)
    elif command[0] == "empty":
        if number == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if number >0:
            print(quelist[front])
        else:
            print(-1)
    elif command[0] == "back":
        if number >0:
            print(quelist[rear-1])
        else:
            print(-1)