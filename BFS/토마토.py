from collections import deque

m,n=map(int, input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

box = []
queue = deque()

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue

            if box[nx][ny]==0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx,ny))

for i in range(n):
    box.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if box[i][j]==1:
            queue.append((i,j))
bfs()
result = 0
edge = 0
for i in range(n):
    for j in range(m):
        if result < box[i][j]:
            result = box[i][j]
        if box[i][j]==0:
            edge = -1

if edge==-1:
    print(-1)
else:
    print(result-1)