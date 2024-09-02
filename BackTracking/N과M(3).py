n,m = map(int, input().split())

ans = []

def track():

    if len(ans)==m:
        print(*ans)
        return
    for i in range(n):
        ans.append(i+1)
        track()
        ans.pop()
track()

# 방향이 없고 중복이 가능하면 for 문으로 돌리면 되는데 그때는 인덱스 아웃 체크를 할 필요가 없다.
# 그리고 따로 배열을 사용한다면 굳이 visited 배열로 방문을 체크할 필요가 없다.
