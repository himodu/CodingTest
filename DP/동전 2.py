from collections import deque

n, k=map(int, input().split())

dp = [-1]*(k+1)
dp[0] = 0

coins = []
for i in range(n):
    coins.append(int(input()))

queue = deque()
queue.append(0)
while queue:
    current = queue.popleft()
    if current == k:
        break
    for i in range(n):
        next = current + coins[i]
        if  next<=k and dp[next] == -1:
            dp[next] = dp[current] + 1
            queue.append(current+coins[i])

print(dp[k])