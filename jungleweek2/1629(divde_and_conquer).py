import sys

A, B, C = map(int, sys.stdin.readline().split())

def divide(a, b, c):
    if b == 0:
        return 1
    temp = divide(a, b // 2, c)
    temp = (temp * temp) % c
    if b % 2 == 0:
        return temp
    else:
        return (temp * a) % c

print(divide(A, B, C))