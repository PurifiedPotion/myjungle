def create_square_matrix(N):
    return [[(i * N) + j + 1 for j in range(N)] for i in range(N)]

N = 2**int(input())
matrix = create_square_matrix(N)
for row in matrix:
    print(row)

#배열 다르면 아래 x,y만 바꾸면됨됨
def Bigblind(x,y,z,h):
if z%4 ==3:
    
    smallblind1(x,y,z)

    matrix[x][y] = z

    smallblind1(x,y,z)

    

def smallblind1(x,y,z):

    z += 1
    x += 1

    matrix[x][y] = z

    smallblind2(x,y,z)

def smallblind2(x,y,z):

    z += 1
    x -=1
    y += 1

    matrix[x][y] = z

    smallblind3(x,y,z)

def smallblind3(x,y,z):

    z += 1
    x += 1

    matrix[x][y] = z

    Bigblind(x,y,z)





Bigblind(0,0,0,0)