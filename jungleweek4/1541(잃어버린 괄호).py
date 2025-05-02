import sys
input = sys.stdin.readline

expression = input().split("-")

total = 0

first = sum(map(int, expression[0].split("+")))
total += first

for part in expression[1:]:
    total -= sum(map(int, part.split("+")))

print(total)