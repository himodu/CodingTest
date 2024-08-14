n,s = map(int, input().split())

list = list(map(int, input().split()))
visited = [False]*n

result = 0

def track(index, sum):
    global result

    if index == n-1:
        if sum+list[index]==s:
            result += 1
        return
    if sum+list[index] == s:
        result += 1

    visited[index] = True
    track(index+1, sum+list[index])

    visited[index] = False
    track(index+1, sum)

track(0,0)
print(result)