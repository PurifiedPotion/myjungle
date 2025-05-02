import sys
input = sys.stdin.readline

class Node:
    def __init__(self, value, left, right):
        self.value = value
        if left != ".":
            self.left = left   # 왼쪽 자식
        else :
            self.left = None
        
        if right != ".":
            self.right = right  # 오른쪽 자식
        else :
            self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

N = int(input())

count = 0

first_nodes = list(map(str, input().split()))

mytree = Node(first_nodes[0], first_nodes[1], first_nodes[2])

print(mytree.value, mytree.left, mytree.right)