import sys

def largest_rectangle(hist):
    stack = []
    max_area = 0
    index = 0
    n = len(hist)

    while index < n:
        # 스택이 비어있거나 현재 높이가 스택 맨 위보다 높으면 push
        if not stack or hist[stack[-1]] <= hist[index]:
            stack.append(index)
            index += 1
        else:
            # 현재 막대가 더 작으면 스택에서 pop하고 넓이 계산
            top = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            area = hist[top] * width
            print(area)
            max_area = max(max_area, area)

    # 남은 것들 처리
    while stack:
        top = stack.pop()
        width = index if not stack else index - stack[-1] - 1
        area = hist[top] * width
        print(area)
        max_area = max(max_area, area)

    return max_area

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if line.strip() == "0":
            break
        nums = list(map(int, line.strip().split()))
        n = nums[0]
        heights = nums[1:]
        print(largest_rectangle(heights))

if __name__ == "__main__":
    main()