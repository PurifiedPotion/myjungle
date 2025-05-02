import sys

t = int(input())

for _ in range(t):
    ps = sys.stdin.readline()
    while True:
        if '()' in ps:
            ps = ps.replace('()', '')
        else:
            break
    if '(' in ps or ')' in ps:
        print('NO')
    else:
        print('YES')