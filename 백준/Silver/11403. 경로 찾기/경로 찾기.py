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

        if current == e and s!=e:
            result[s][e] = 1
            break
        for i in range(n):
            if graph[current][i]==1 and not visited[i]:
                if e == i:
                    result[s][e]=1
                visited[i] = True
                stack.append(i)

for i in range(n):
    for j in range(n):
        visited = [False]*n
        if dfs(i,j,visited)==True:
            result[i][j] = 1


for i in range(n):
    print(*result[i])