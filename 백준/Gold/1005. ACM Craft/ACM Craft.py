from collections import deque

def bfs(graph,time,goal,isStart):

    queue = deque()
    stackTime = time.copy()

    for i in range(len(isStart)):
        if isStart[i]:
            queue.append(i+1)

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if stackTime[i-1] < stackTime[node-1]+time[i-1]:
                    stackTime[i-1] = stackTime[node-1]+time[i-1]
                    queue.append(i)

    return stackTime[goal-1]

t = int(input())

result = []

for i in range(t):
    n,k = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    time = list(map(int, input().split()))

    isStart = [True]*n
    for j in range(k):
        start, end = map(int, input().split())
        isStart[end-1] = False
        graph[start].append(end)

    goal = int(input())

    result.append(bfs(graph, time, goal, isStart))

for i in result:
    print(i)
