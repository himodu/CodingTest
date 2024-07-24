n = int(input())

stairs = []
stairs.append(0)
dp = [0]*(n+1)

for i in range(n):
    stairs.append(int(input()))

for i in range(1,n+1):

    if i==1:
        dp[i] = stairs[i]
        continue
    if i==2:
        dp[i] = stairs[i]+stairs[i-1]
        continue

    max = 0
    if stairs[i]+stairs[i-1]+dp[i-3] > max:
        max = stairs[i]+stairs[i-1]+dp[i-3]

    if stairs[i]+dp[i-2] > max:
        max = stairs[i]+dp[i-2]

    dp[i] = max

print(dp[n])