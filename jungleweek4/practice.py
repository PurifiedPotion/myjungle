import sys
input = sys.stdin.readline

n = int(input())

memo = {0 : 0, 1 : 1, 2 : 1, 3 : 1, 4 : 2, 5 : 5, 6 : 8, 7 : 13, 8 : 21, 9 : 34, 10 : 55, 11 : 89, 12 : 144, 13 : 233, 14 : 377, 15 : 610}

def fib(n):
	if n in memo:
		return memo[n]
	else:
		memo[n] = fib(n-1) + fib(n-2)
		return memo[n]

print(fib(n))