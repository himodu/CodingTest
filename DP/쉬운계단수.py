n = int(input())

dp = [[0]*(10) for _ in range(n+1)]

for i in range(10):
    if i != 0:
        dp[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        if j==0:
            dp[i][j] += dp[i-1][j+1]
            continue
        if j==9:
            dp[i][j] += dp[i-1][j-1]
            continue

        dp[i][j] += (dp[i-1][j-1]+dp[i-1][j+1])

result = 0
for i in range(10):
    result += dp[n][i]

print(result%1000000000)