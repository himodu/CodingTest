t = int(input())

def solution(case, n):
    dp = [[0]*(n+1) for _ in range(2)]
    dp[0][1] = case[0][0]
    dp[1][1] = case[1][0]

    for i in range(2, n+1):
        for j in range(2):

            if dp[(j+1)%2][i-1] >= max(dp[0][i-2], dp[1][i-2]):
                dp[j][i] = dp[(j+1)%2][i-1] + case[j][i-1]
            else:
                dp[j][i] = max(dp[0][i-2], dp[1][i-2])+ case[j][i-1]
    return max(dp[0][n], dp[1][n])

result = []

for i in range(t):
    n = int(input())
    case = [list(map(int, input().split())) for _ in range(2)]
    result.append(solution(case, n))

for ans in result:
    print(ans)