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

################################# KNAPSHACK PROBLEM ##################################
# 2차원 (가방 무게, 물건) 2개의 축으로 나눠서 dp 테이블 생성
# 1. 무게가 딸려서 못넣는 경우
#     이 경우도 직전에 것을 가져온다.
# 2. 무게가 안 딸려서 넣는 경우
#     1 - 자기 자신을 넣었을 때의 가치 (이거는 직전 정보중 자신을 넣을 수 있을 때의 가치)
#     2 - 자기 직전에 저장된 가치
######################################################################################