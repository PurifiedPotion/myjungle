import sys

charlist = [int(sys.stdin.readline().strip()) for _ in range(9)]

a=0
b=1
c=2
d=3
e=4
f=5
g=6

final_list = []

def addup(a, b, c, d, e, f, g):
    if charlist[a]+charlist[b]+charlist[c]+charlist[d]+charlist[e]+charlist[f]+charlist[g] == 100:
        final_list.append(charlist[a])
        final_list.append(charlist[b])
        final_list.append(charlist[c])
        final_list.append(charlist[d])
        final_list.append(charlist[e])
        final_list.append(charlist[f])
        final_list.append(charlist[g])
        final_list.sort()
        for i in final_list:
            print(i)

    else:
        if g<8:
            addup(a, b, c, d, e, f, g+1)
        elif f<7:
            addup(a, b, c, d, e, f+1, f+2)
        elif e<6:
            addup(a, b, c, d, e+1, e+2, e+3)
        elif d<5:
            addup(a, b, c, d+1, d+2, d+3, d+4)
        elif c<4:
            addup(a, b, c+1, c+2, c+3, c+4, c+5)
        elif b<3:
            addup(a, b+1, b+2, b+3, b+4, b+5, b+6)
        elif a<2:
            addup(a+1, a+2, a+3, a+4, a+5, a+6, a+7)

addup(a, b, c, d, e, f, g)