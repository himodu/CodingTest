import sys
sys.setrecursionlimit(10**6)
n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dp = [[-1]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1,0 ,-1]

def dfs(x,y):
    if x==n-1 and y==m-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    ways = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[x][y] > graph[nx][ny]:
                ways += dfs(nx,ny)

    dp[x][y] = ways
    return dp[x][y]

print(dfs(0,0))

