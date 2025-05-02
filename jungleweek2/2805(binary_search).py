import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

def lets_cut(treelist, length_of_cut, min_height_of_cutter, max_height_of_cutter, result=0):
    if min_height_of_cutter > max_height_of_cutter:
        return result

    cutter_height = (min_height_of_cutter + max_height_of_cutter) // 2
    total_cut = sum((i - cutter_height) for i in treelist if i > cutter_height)

    if total_cut >= length_of_cut:
        return lets_cut(treelist, length_of_cut, cutter_height + 1, max_height_of_cutter, cutter_height) #cutter height를를
    else:                                                                                                #1개씩 줄여나가야
        return lets_cut(treelist, length_of_cut, min_height_of_cutter, cutter_height - 1, result)        #근삿값을 구할 수 있고 이게

print(lets_cut(trees, M, 0, max(trees)))                                                                 #정석이다
