import sys

def comparison(pslist,stklist,ptr,count):

    if len(pslist) == count and ptr == 0:
        return "YES"
    else:
        while count < len(pslist):
            if pslist[count] == "(":
                stklist[ptr] = pslist[count]
                ptr+=1
                count+=1
                return comparison(pslist,stklist,ptr,count)
            elif pslist[count] == ")":
                if ptr==0:
                    return "NO"
                else:
                    ptr-=1
                    count+=1
                    return comparison(pslist,stklist,ptr,count)
        return "NO"

n=int(sys.stdin.readline())

for i in range(n):
    second = list(sys.stdin.readline().strip())
    stklist=[None]*len(second)
    if len(second)%2 != 0:
        print("NO")
    else:
        ptr=0
        final=comparison(second,stklist,ptr,0)
        print(final)