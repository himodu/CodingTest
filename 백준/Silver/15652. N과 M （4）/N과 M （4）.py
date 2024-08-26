n,m = map(int, input().split())

ans = []
def track(index):

    if index==n+1:
        if len(ans)==m:
            for i in range(m):
                print(ans[i], end=' ')
            print()
        return

    if len(ans)==m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return

    for i in range(index, n+1):
        ans.append(i)
        track(i)
        ans.pop()

track(1)