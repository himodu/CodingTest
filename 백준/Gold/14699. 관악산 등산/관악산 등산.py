import heapq
n,m = map(int, input().split())
height = list(map(int, input().split()))

heap = []
for i in range(n):
    heapq.heappush(heap, (-height[i], i+1))
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)

for i in range(m):
    s, e = map(int, input().split())
    if height[s-1] > height[e-1]:
        graph[s].append(e)
    else:
        graph[e].append(s)

def dfs(start):
    stack = [start]
    stack.append(start)
    while stack:
        current = stack.pop()
        for i in graph[current]:
            if visited[i] < visited[current] + 1:
                stack.append(i)
                visited[i] = visited[current] + 1
index = 0
while heap:
    height, start = heapq.heappop(heap)
    if visited[start]==0:
        index += 1
        visited[start] += 1
        dfs(start)

for i in range(1,n+1):
    print(visited[i])