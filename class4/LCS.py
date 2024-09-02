str1 = input()
str2 = input()

len1 = len(str1)
len2 = len(str2)

dp = [[0]*len2 for _ in range(len1)]

for i in range(len1):
    if str1[i] == str2[0]:
        dp[i][0] = 1
    else:
        if i > 0 and dp[i-1][0] == 1:
            dp[i][0] = 1
        else:
            dp[i][0] = 0

for i in range(len2):
    if str2[i] == str1[0]:
        dp[0][i] = 1
    else:
        if i > 0 and dp[0][i-1] == 1:
            dp[0][i] = 1
        else:
            dp[0][i] = 0

for i in range(1, len1):
    for j in range(1, len2):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            max = 0
            if max < dp[i-1][j]:
                max = dp[i-1][j]
            if max < dp[i][j-1]:
                max = dp[i][j-1]
            dp[i][j] = max

print(dp[len1-1][len2-1])