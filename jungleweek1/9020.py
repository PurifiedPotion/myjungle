for i in range(int(input())):
    less=int(input())
    lesslist=[]
    primenumbers=[]
    for j in range(less):
        if j!=0 and j!=1:
            lesslist.append(j)
    print(lesslist)
    for k in range(len(lesslist)):
        for l in range(1,lesslist[k]):
            if lesslist[k]==2:
                primenumbers.append(lesslist[k])
                continue
            if lesslist[k]%(l+1)==0:
                break
            if lesslist[k]==l+2:
                primenumbers.append(lesslist[k])
    print(primenumbers)
    for m in primenumbers:
        for n in primenumbers:
            if m+n==less:
                print(m,n)