from collections import deque
t = int(input())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

field = []
visited = []

def bfs(n,m, x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            if not visited[nx][ny] and field[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny))

resultList = []
for i in range(t):
    n,m,c = map(int, input().split())

    field = [[0]*m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for j in range(c):
        x, y = map(int, input().split())
        field[x][y] = 1

    result = 0
    for k in range(n):
        for l in range(m):
            if not visited[k][l] and field[k][l]==1:
                bfs(n,m,k,l)
                result += 1

    resultList.append(result)


for i in range(len(resultList)):
    print(resultList[i])