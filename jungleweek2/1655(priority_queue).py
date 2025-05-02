import sys
import heapq

n=int(sys.stdin.readline())
min_heap = [] # 큰 수들을 저장 (최소 힙)
max_heap = [] # 작은 수들을 저장 (최대 힙, 파이썬은 최소 힙만 지원하므로 음수로 저장)


for _ in range(n):
    second = int(sys.stdin.readline())

    # max_heap에 먼저 넣는다 (음수로 넣어서 최대 힙처럼 동작)
    if not max_heap or second <= -max_heap[0]:
        heapq.heappush(max_heap, -second)
    else:
        heapq.heappush(min_heap, second)
    
    # 두 힘의 균형 조절
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    # 중간값은 항상 max_heap의 루트
    print(-max_heap[0])