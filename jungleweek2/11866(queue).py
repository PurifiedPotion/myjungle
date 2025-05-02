import sys
from typing import Any

class FixedQueue:

    class Empty(Exception):
        """비어 있는 FixedQueue에 대해 deque 또는 peek를 호출할 때 내보내는 예외처리"""
        pass

    class Full(Exception):
        """가득 찬 FixedQueue에 enque를 호출할 때 내보내는 예외처리"""
        pass

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity
    
    def enque(self, x: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x
    
    def __init__(self, capacity: int) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

n, k = map(int, sys.stdin.readline().split())

q = FixedQueue(n)

for i in range(1, n + 1):
    q.enque(i)

count = 0
final_list = []

while count < n:
    if q.no == 0:
        break  # 💥 q.no == 0이면 루프 탈출 (ZeroDivisionError 방지)

    # k번째까지 회전 (k-1번만 회전 후 k번째 제거)
    for _ in range(k - 1):
        q.enque(q.deque())

    final_list.append(q.deque())  # k번째 제거
    count += 1

print("<" + ", ".join(map(str, final_list)) + ">")