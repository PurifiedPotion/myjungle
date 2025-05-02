from __future__ import annotations
from typing import Any, Type
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 혹시 재귀 깊이 문제 방지

class Node:
    """이진 검색 트리의 노드"""
    def __init__(self, key: Any, left: Node = None, right: Node = None):
        """생성자"""
        self.key = key      # 키
        self.left = left    # 왼쪽 포인터(왼쪽 자식 참조)
        self.right = right  # 오른쪽 포인터(오른쪽 자식 참조)

class BinarySearchTree:
    """이진 검색 트리"""

    def __init__(self):
        """초기화"""
        self.root = None  # 루트

# Do it! 실습 9-1[C]
    def add(self, key: Any) -> bool:
        """키가 key이고, 값이 value인 노드를 삽입"""

        def add_node(node: Node, key: Any) -> None:
            """node를 루트로 하는 서브 트리에 키가 key이고, 값이 value인 노드를 삽입"""
            if key == node.key:
                return False  # key가 이진검색트리에 이미 존재
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, None, None)
                else:
                    add_node(node.left, key)
            else:
                if node.right is None:
                    node.right = Node(key, None, None)
                else:
                    add_node(node.right, key)
            return True

        if self.root is None:
            self.root = Node(key, None, None)
            return True
        else:
            return add_node(self.root, key)

# Do it! 실습 9-1[E]
    def dump(self) -> None:
        """덤프(모든 노드를 키의 오름차순으로 출력)"""

        def print_subtree(node: Node):
            """node를 루트로 하는 서브 트리의 노드를 키의 오름차순으로 출력"""
            if node is not None:
                print_subtree(node.left)            # 왼쪽 서브 트리를 오름차순으로 출력
                print_subtree(node.right)           # 오른쪽 서브 트리를 오름차순으로 출력
                print(f'{node.key}')  # node를 출력

        print_subtree(self.root)

tree = BinarySearchTree()

# 입력 받기
for i in sys.stdin:
    i = i.strip()
    if i == '':
        continue
    tree.add(int(i))

tree.dump()