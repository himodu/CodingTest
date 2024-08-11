n, m=map(int, input().split())

nums = [i+1 for i in range(n)]
visited = [False]*n

def back(start, count):
    if start > n-1 and count != m:
        return
    if count == m:
        for i in range(n):
            if visited[i]:
                print(nums[i], end=' ')
        print()
        return

    visited[start] = True
    back(start+1, count+1)

    visited[start] = False
    back(start+1, count)

back(0,0)