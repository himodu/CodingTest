n, d=map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

count = 0
for i in range(n):
    if coins[n-1-i] <= d and d > 0:
        count += int(d/coins[n-1-i])
        d = d % coins[n-1-i]

print(count)