import sys
input = sys.stdin.readline

n = int(input())

memo = {0: 0, 1: 1}

def fib(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    
print(fib(n))