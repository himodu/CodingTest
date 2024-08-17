n,m = map(int, input().split())

visited = [False]*n
ans = []

def track(index):

    if index == n:
        if len(ans)==m:
            print(*ans)
        return

    if len(ans)==m:
        print(*ans)
        return

    for i in range(n):
        visited[i] = True
        ans.append(i+1)
        track(i)
        visited[i] = False
        ans.pop()

track(0)