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

# 이 문제는 bfs를 진행하는 시점이 여러개인 경우에 대한 문제이다.
# 큐에다가 시작 지점을 그냥 다 넣어두고, 탐색을 실행 하면된다.
# 일종의 전염 시뮬레이션 문제인데, 여러 군데에서 시작을 하더라도, 이미 전염된 칸은 방문하지 않고,# 전염 확산을 시뮬레이
# 서로 한 칸씩만 진행되기 때문에 전염 확산 기간을 확인할 수 있다.
