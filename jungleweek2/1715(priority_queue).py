import sys
import heapq

n = int(sys.stdin.readline())
arr = []

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

arr = []

for _ in range(n):
    second = int(sys.stdin.readline())
    arr.append(second)

final_list = heapsort(arr)

count=0
while len(final_list)>1:
    s = heapq.heappop(final_list) + heapq.heappop(final_list)
    count += s
    heapq.heappush(final_list, s)

print(count)
