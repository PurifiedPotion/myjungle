a=int(input())
first_top_list=[]
second_top_list=[]
third_top_list=[]
trail_of_moving=[]
move_list=[]


def list_first_top(n):
    for i in range(n):
        first_top_list.append(i+1)

list_first_top(a)
print(first_top_list)

def move(o):
    if o==12:
        if first_top_list[0]<second_top_list[0] or len(second_top_list)==0:
            second_top_list.append(first_top_list[0])
            second_top_list.sort()
            del first_top_list[0]
            trail_of_moving.append("1 2")
    elif o==13:
        if first_top_list[0]<third_top_list[0] or len(third_top_list)==0:
            third_top_list.append(first_top_list[0])
            third_top_list.sort()
            del first_top_list[0]
            trail_of_moving.append("1 3")
    elif o==21:
        if second_top_list[0]<first_top_list[0] or len(first_top_list)==0:
            first_top_list.append(second_top_list[0])
            first_top_list.sort()
            del second_top_list[0]
            trail_of_moving.append("2 1")
    elif o==23:
        if second_top_list[0]<third_top_list[0] or len(third_top_list)==0:
            third_top_list.append(second_top_list[0])
            third_top_list.sort()
            del second_top_list[0]
            trail_of_moving.append("2 3")
    elif o==31:
        if third_top_list[0]<first_top_list[0] or len(first_top_list)==0:
            first_top_list.append(third_top_list[0])
            first_top_list.sort()
            del third_top_list[0]
            trail_of_moving.append("3 1")
    elif o==32:
        if third_top_list[0]<second_top_list[0] or len(second_top_list)==0:
            second_top_list.append(third_top_list[0])
            second_top_list.sort()
            del third_top_list[0]
            trail_of_moving.append("3 2")
    else: pass


for p in range(1,4):
    for q in range(1,4):
        move_list.append(int(f"{p}"+f"{q}"))


print(first_top_list)
print(second_top_list)
print(third_top_list)
print(move_list)