n = int(input())

rgbs = []

for i in range(n):
    rgbs.append(list(map(int, input().split())))

dp = [[0,0,0] for _ in range(n)]

dp[0][0] = rgbs[0][0]
dp[0][1] = rgbs[0][1]
dp[0][2] = rgbs[0][2]

for i in range(1, n):
    for j in range(3):
        min = 10e9
        if dp[i-1][(j+1)%3] < min:
            min = dp[i-1][(j+1)%3]
        if dp[i-1][(j+2)%3] < min:
            min = dp[i-1][(j+2)%3]

        dp[i][j] = rgbs[i][j]+ min

min = 10e9
for i in range(3):
    if min > dp[n-1][i]:
        min = dp[n-1][i]

print(min)