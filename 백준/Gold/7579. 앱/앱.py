n,m = map(int, input().split())


onMem = list(map(int, input().split()))

cost = list(map(int, input().split()))

data = []
for i in range(n):
    data.append((onMem[i], cost[i]))

dp = [[0]*(n+1) for _ in range(sum(cost)+1)]

for i in range(sum(cost)+1):
    if i >= data[0][1]:
        dp[i][1] = data[0][0]

result = 10e9

for i in range(1, n+1):
    mem, cos = data[i-1]
    for j in range(sum(cost)+1):
        if cos <= j:
            dp[j][i] = max(dp[j][i-1], dp[j-cos][i-1]+mem)
        else:
            dp[j][i] = dp[j][i-1]

        if m <= dp[j][i]:
            result = min(result, j)

print(result)