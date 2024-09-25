import sys
sys.setrecursionlimit(10**6)

t = int(input())

def dfs(index):
    global result
    visited[index] = True
    cycle.append(index)

    nindex = graph[index] - 1

    if not visited[nindex]:
        dfs(nindex)
    else:
        if nindex in cycle:
            result += cycle[cycle.index(nindex):]
        return

finalResult = []

for i in range(t):
    n = int(input())
    graph = list(map(int, input().split()))
    visited = [False] * n
    result = []

    for j in range(n):
        if not visited[j]:
            cycle=[]
            dfs(j)

    finalResult.append(n - len(result))

for res in finalResult:
    print(res)