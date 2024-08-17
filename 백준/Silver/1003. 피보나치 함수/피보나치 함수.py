n = int(input())

test = []
dp = [0]*41

dp[0] = 0
dp[1] = 1

def fibo(num):
    global zero, one
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        if dp[num] != 0:
            return dp[num]
        else:
            dp[num] = fibo(num - 1) + fibo(num - 2)
            return dp[num]

for i in range(n):
    test.append(int(input()))

for i in range(n):
    zero = 0
    one = 0
    num = test[i]

    fibo(num)
    if test[i]==0:
        print(1,0)
    else:
        print(dp[num-1], dp[num])
