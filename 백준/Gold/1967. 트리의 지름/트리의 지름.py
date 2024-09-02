import sys
sys.setrecursionlimit(10**9)

n = int(input())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    s, e, p = map(int, input().split())
    graph[s].append((e,p))
    graph[e].append((s,p))

def dfs(start, weight):
    for node, point in graph[start]:
        if distance[node]==-1:
            distance[node] = weight + point
            dfs(node, weight + point)

distance = [-1]*(n+1)
distance[1] = 0
dfs(1,0)

maxVar = 0
start = 0
for i in range(len(distance)):
    if maxVar < distance[i]:
        maxVar = distance[i]
        start = i

distance = [-1]*(n+1)
distance[start] = 0
dfs(start,0)

print(max(distance))