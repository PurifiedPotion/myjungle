import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# 입력 전체를 받아 리스트로 변환
preorder = []
while True:
    line = input()
    if not line:
        break
    preorder.append(int(line.strip()))

# 후위 순회 (postorder) 결과를 담을 리스트
result = []

def postorder(start, end):
    if start >= end:
        return

    root = preorder[start]
    idx = start + 1

    # 오른쪽 서브트리의 시작 찾기
    while idx < end and preorder[idx] < root:
        idx += 1

    postorder(start + 1, idx)  # 왼쪽 서브트리
    postorder(idx, end)        # 오른쪽 서브트리
    result.append(root)        # 현재 노드

postorder(0, len(preorder))

# 결과 출력
sys.stdout.write('\n'.join(map(str, result)))
