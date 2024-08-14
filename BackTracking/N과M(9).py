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

# 이 문제 같은 경우 기존에 백트래킹 문제는
# 탐색 방향이 한 방향이었었는데 앞 뒤 모두 탐색을 하려면 어떻게 해야할까? 에 대한 고민을 해결한 문제
# 방문처리 꼼꼼히 해주고, 중복 탐색을 막아주고 모든 노드를 for 문으로 돌리면 모든 방향으로 탐색이 가능하다.
