import sys
sys.setrecursionlimit(10**6)  # 혹시 재귀 깊이 문제 방지

# 입력 받기
n = int(input())
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

# 전위 순회 (Preorder): 루트 -> 왼쪽 -> 오른쪽
def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

# 중위 순회 (Inorder): 왼쪽 -> 루트 -> 오른쪽
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])

# 후위 순회 (Postorder): 왼쪽 -> 오른쪽 -> 루트
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')

# 순회 시작 (항상 루트는 'A')
preorder('A')
print()
inorder('A')
print()
postorder('A')
