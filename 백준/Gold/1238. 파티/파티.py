import heapq

n,m,x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    s,e,t = map(int, input().split())
    graph[s].append((e,t))


def dijkstart(start):
    q = []
    heapq.heappush(q, (0, start))
    timeTable = [1e9]*(n+1)
    timeTable[start] = 0

    while q:
        time, node = heapq.heappop(q)

        if timeTable[node] < time:
            continue

        for nextNode, nextTime  in graph[node]:
            cost = time + nextTime
            if cost < timeTable[nextNode]:
                timeTable[nextNode] = cost
                heapq.heappush(q, (cost, nextNode))

    return timeTable

result = 0

back = dijkstart(x)

for i in range(n):

    toGo = dijkstart(i+1)
    if result < toGo[x] + back[i+1]:
        result = toGo[x] + back[i+1]

print(result)