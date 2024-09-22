import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e,c))


start, end = map(int, input().split())

distance = [1e9] * (n+1)
prev_node = [0] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for adjNode, adjDist in graph[node]:
            cost = dist + adjDist
            if cost < distance[adjNode]:
                distance[adjNode] = cost
                prev_node[adjNode] = node
                heapq.heappush(q, (cost, adjNode))



dijkstra(start)

ans = []

node = end

while node!=start:
    ans.append(node)
    node = prev_node[node]

ans.append(start)
ans.reverse()

print(distance[end])
print(len(ans))
print(*ans)
