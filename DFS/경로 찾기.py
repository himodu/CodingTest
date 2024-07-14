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

# 이 문제는 DFS를 익히기 위해 푼 문제
# DFS라고 해서 굳이 재귀를 쓸 필요가 없고, 솔직히 BFS랑 비교했을 때 큰 차이가 없다는 걸 느낌
