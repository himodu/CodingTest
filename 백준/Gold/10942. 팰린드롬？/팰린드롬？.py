n = int(input())

data = list(map(int, input().split()))

t = int(input())

dp = [[0]*n for _ in range(n)]




for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if data[i] == data[i+1]:
        dp[i][i+1] = 1

for i in range(2, n):
    for j in range(n-i):
        if dp[j+1][j+i-1] == 1 and data[j]==data[j+i]:
            dp[j][j+i] = 1

result = []

for i in range(t):
    start, end = map(int, input().split())
    result.append(dp[start-1][end-1])

for res in result:
    print(res)