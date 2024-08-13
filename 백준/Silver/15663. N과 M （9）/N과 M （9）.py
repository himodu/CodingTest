n, m = map(int, input().split())

data = sorted(list(map(int, input().split())))
visited = [False]*n

answer = []

def dfs():

    if len(answer)==m:
        print(*answer)
        return
    remember = 0
    for i in range(n):
        if not visited[i] and remember != data[i]:
            visited[i]=True
            answer.append(data[i])
            remember = data[i]
            dfs()
            visited[i]=False
            answer.pop()

dfs()