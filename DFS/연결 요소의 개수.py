n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = 0

def dfs(start):
    stack = [start]
    stack.append(start)
    while stack:
        current = stack.pop()
        for i in graph[current]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True

for i in range(m):
    s, e=map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited[0] = True
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        result += 1

print(result)

# 이 문제는 DFS 를 좀 더 이해하기 위한 문제
# 이거도 마찬가지로 BFS랑 차이를 모르겠다.
