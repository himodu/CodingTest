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

# 이 문제는 단순히 DFS 를 돌리는 게 다가 아님
# DFS/BFS 는 시간 복잡도가 O(n) 인데 N=5000 인 상황에서 모든 노드에서 탐색을 진행하면 O(n^2) 이니까 1초가 넘음
# 그래서 방문하지 않은 노드만 탐색을 진행해주는 걸로 했고, (이 정도만 해줘도 n^2 충분히 해결 가능)포인트는 등산이라고 해서 낮은 부분에서부터 시작하는게 아니라 
# 정상 즉, 그 경로의 목적지에서 내려와야 그 경로의 value 를 파악하기 용이하다라는 점이 중요하고 그래서 노드들을 heap에 저장해서 
# 높이가 높은 거 부터 차례로 빼내는 게 중요하다.
