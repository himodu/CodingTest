n = int(input())

matrix = []

for i in range(n):
    n1, n2 = map(int, input().split())
    matrix.append((n1,n2))

dp = [[0]*n for _ in range(n)]

for i in range(n-1):
    dp[i][i+1] = matrix[i][0]*matrix[i][1]*matrix[i+1][1]

for i in range(2, n):
    for j in range(n-i):
        dp[j][j+i] = 2**32
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k]+dp[k+1][j+i]+matrix[j][0]*matrix[k][1]*matrix[j+i][1])

print(dp[0][n-1])