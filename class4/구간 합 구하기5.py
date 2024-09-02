n,m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(n+1) for _ in range(n)]

for i in range(n):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + data[i][j-1]

def cacul(x1,y1,x2,y2):
    result = 0
    for i in range(x1, x2+1):
        result += dp[i][y2+1] - dp[i][y1+1] + data[i][y1]
    return result

result = []

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result.append(cacul(x1-1,y1-1,x2-1,y2-1))

for i in range(m):
    print(result[i])