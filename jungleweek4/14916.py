# 성공

import sys
input = sys.stdin.readline

n = int(input())
count = 0

if n >= 5 and (n%5)%2 == 0:
    count += n // 5
    n %= 5
elif n >= 5:
    count += (n//5)-1
    n %= 5
    n += 5

if n >= 2:
    count += n // 2
    n %= 2

if n != 0 :
    count = -1

print(count)