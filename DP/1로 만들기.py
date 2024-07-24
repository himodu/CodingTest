n = int(input())

dp = [-1]*(n+1)
dp[1] = 0

for i in range(2, n+1):
    min = 1000000
    if dp[i//2] != -1 and i%2==0:
        if min > dp[i//2]:
            min = dp[i//2]
    if dp[i//3] != -1 and i%3==0:
        if min > dp[i//3]:
            min = dp[i // 3]
    if min > dp[i-1]:
        min = dp[i-1]

    dp[i] = min + 1

print(dp[n])