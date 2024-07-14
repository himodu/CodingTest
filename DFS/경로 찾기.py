from collections import deque

n = int(input())

graph = []
result = [[0]*n for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(s, e, visited):
    stack = deque()
    stack.append(s)
    while stack:
        current = stack.pop()
        for i in range(n):
            if graph[current][i]==1 and not visited[i]:
                if e == i:
                    result[s][e]=1
                visited[i] = True
                stack.append(i)

for i in range(n):
    for j in range(n):
        visited = [False]*n
        dfs(i,j,visited)

for i in range(n):
    print(*result[i])