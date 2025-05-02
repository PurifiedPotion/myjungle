n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

def can_install(distance):
    count = 1
    last_installed = houses[0]

    for i in range(1, n):
        if houses[i] - last_installed >= distance:
            count += 1
            last_installed = houses[i]
    
    return count >= c

low = 1
high = houses[-1] - houses[0]
result = 0

while low <= high:
    mid = (low + high) // 2
    if can_install(mid):
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
