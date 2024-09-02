n,k = map(int, input().split())

burdens = []

for i in range(n):
    w,v = map(int, input().split())
    burdens.append((w,v))

dp = [[0]*(n+1) for _ in range(k+1)]

for i in range(1, n+1):
    cw, cv = burdens[i-1]
    for j in range(1, k+1):
        if cw <= j:
            if dp[j][i-1] > dp[j-cw][i-1]+cv:
                dp[j][i] = dp[j][i-1]
            else:
                dp[j][i] = dp[j-cw][i-1]+cv
        else:
            dp[j][i] = dp[j][i-1]

print(dp[k][n])