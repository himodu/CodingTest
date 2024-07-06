from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        distance[x][y] += 1
        if x==n-1 and y==m-1:
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            if not visited[nx][ny] and list[nx][ny]=='1':
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y]
                queue.append((nx, ny))

n, m = map(int, input().split())

list = []
visited = [[0]*m for _ in range(n)]
distance = [[0]*m for _ in range(n)]

for i in range(n):
    list.append(input())

bfs(0,0)
print(distance[n-1][m-1])

# 이 문제는 bfs 기초적인 감을 찾기 위해서 푼 문제
# 아주 기초적인 좌표형 bfs 문제이다.
