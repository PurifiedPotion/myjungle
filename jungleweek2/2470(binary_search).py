import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

left = 0
right = n - 1
min_sum = float('inf')
answer = (0, 0)

while left < right:
    total = arr[left] + arr[right]

    if abs(total) < min_sum:
        min_sum = abs(total)
        answer = (arr[left], arr[right])

    if total < 0:
        left += 1
    else:
        right -= 1

print(answer[0], answer[1])
