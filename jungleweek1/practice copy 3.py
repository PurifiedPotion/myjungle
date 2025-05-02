import sys
from typing import MutableSequence

def sort3(a: MutableSequence, idx1, idx2, idx3):
    """ 세 개의 원소를 정렬하고 중앙값의 인덱스를 반환 """
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2

def insertion_sort(a: MutableSequence, left, right):
    """ 삽입 정렬 (부분 정렬을 위해 left, right 추가) """
    for i in range(left + 1, right + 1):
        j = i
        tmp = a[i]
        while j > left and a[j - 1] > tmp:  # j > left로 수정
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

def qsort(a: MutableSequence, left, right):
    """ 퀵 정렬 (피벗을 중앙값으로 선정) """
    if right - left < 9:
        insertion_sort(a, left, right)
        return  # 추가: 삽입 정렬 후 재귀가 불필요

    pl = left
    pr = right
    m = sort3(a, pl, (pl+pr) // 2, pr)  # 중앙값을 피벗으로 선택
    x = a[m]

    # 피벗을 오른쪽에서 두 번째 위치로 이동
    a[m], a[pr - 1] = a[pr - 1], a[m]
    pl += 1
    pr -= 2  # 기존 `pr -= 1`에서 `pr -= 2`로 수정

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    qsort(a, left, pr)  # 왼쪽 부분 정렬
    qsort(a, pl, right)  # 오른쪽 부분 정렬

def quick_sort(a: MutableSequence):
    """ 퀵 정렬 호출 함수 """
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    input_data = sys.stdin.read().split()  # 전체 입력을 읽고 공백 기준으로 나누기
    num = int(input_data[0])  # 첫 번째 값은 원소 개수
    x = list(map(int, input_data[1:num+1]))  # 나머지 값들을 정수 리스트로 변환

    quick_sort(x)

    print("\n".join(map(str, x)))  # 정렬된 결과를 출력
