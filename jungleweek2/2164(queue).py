import sys

n = int(sys.stdin.readline())

quelist=[]

for i in range(n):
    quelist.append(i+1)

front = rear = 0
number = n
capacity = n

while number>1:
    front += 1
    front = front%capacity
    number -= 1

    quelist[front], quelist[rear] = quelist[rear], quelist[front]

    rear += 1
    rear = rear%capacity
    front += 1
    front = front%capacity

print(quelist[front])