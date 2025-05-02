# 2504. 괄호의 값
import sys
s = sys.stdin.readline().strip()
stack = []
for char in s:
    if char in '([':
        stack.append(char)
    else:
        if not stack:
            print(0)
            exit()
        temp = 0
        while stack:
            top = stack.pop()
            if isinstance(top, int): # 어떤 값이 특정 자료형인지 확인하는 함수
                temp += top
            else:
                if (char == ')' and top == '(') or (char == ']' and top == '['):
                    value = 2 if char == ')' else 3
                    stack.append(value if temp == 0 else value * temp)
                    break
                else:
                    print(0)
                    exit()
        else:
            print(0)
            exit()
result = 0
for item in stack:
    if isinstance(item, int):
        result += item
    else:
        print(0)
        exit()
print(result)