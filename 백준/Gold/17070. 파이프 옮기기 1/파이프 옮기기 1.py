n = int(input())

field = []
for i in range(n):
    field.append(list(map(int, input().split())))

# field[0][0] = 2
# field[0][1] = 2

# garo = [[0,1],[1,1]]
# garoNext = [2,4]
# sero = [[1,1],[0,1]]
# seroNext = [3,4]
# degac = [[0,1,1],[1,0,1]]
# degacNext = [2,3,4]

def moveToGaro(x,y):
    nx, ny = x, y+1
    if 0<=nx<n and 0<=ny<n and not field[nx][ny]==1:
        dfs(nx,ny,2)

def moveToSero(x,y):
    nx, ny = x+1, y
    if 0<=nx<n and 0<=ny<n and not field[nx][ny]==1:
        dfs(nx,ny,3)

def moveToDegac(x,y):
    nx, ny = x+1, y+1
    if 0<=nx<n and 0<=ny<n and not field[nx][ny]==1:
        if not field[nx - 1][ny] == 1 and not field[nx][ny - 1] == 1:
            dfs(nx,ny,4)

def dfs(x,y,dir):
    global result
    if x==(n-1) and y==(n-1):
        result += 1
        return
    if dir==2:
        moveToGaro(x,y)
        moveToDegac(x,y)
    elif dir==3:
        moveToSero(x,y)
        moveToDegac(x,y)
    elif dir==4:
        moveToGaro(x,y)
        moveToSero(x,y)
        moveToDegac(x,y)

    # if field[x][y]==2:
    #     for i in range(2):
    #         nx,ny = x+garo[0][i], y+garo[1][i]
    #         if 0<=nx<n and 0<=ny<n and not field[nx][ny]==1:
    #                 field[nx][ny] = garoNext[i]
    #                 if garoNext[i]==4:
    #                     if not field[nx-1][ny]==1 and not field[nx][ny-1]==1:
    #                         dfs(nx, ny)
    #                 else:
    #                     dfs(nx,ny)
    #                 field[nx][ny] = 0
    # elif field[x][y]==3:
    #     for i in range(2):
    #         nx,ny = x+sero[0][i], y+sero[1][i]
    #         if 0<=nx<n and 0<=ny<n and not field[nx][ny]==1:
    #                 field[nx][ny] = seroNext[i]
    #                 if seroNext[i]==4:
    #                     if not field[nx-1][ny]==1 and not field[nx][ny-1]==1:
    #                         dfs(nx, ny)
    #                 else:
    #                     dfs(nx,ny)
    #                 field[nx][ny] = 0
    # elif field[x][y]==4:
    #     for i in range(3):
    #         nx,ny = x+degac[0][i], y+degac[1][i]
    #         if 0<=nx<n and 0<=ny<n and not field[nx][ny]==1:
    #                 field[nx][ny] = degacNext[i]
    #                 if degacNext[i]==4:
    #                     if not field[nx-1][ny]==1 and not field[nx][ny-1]==1:
    #                         dfs(nx, ny)
    #                 else:
    #                     dfs(nx,ny)
    #                 field[nx][ny] = 0

result = 0
dfs(0,1,2)
print(result)