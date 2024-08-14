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

# 이 문제는 백트래킹을 처음 다뤄본 문제이다.
# 백트래킹의 핵심은 탐색인데, 지금 탐색하는 노드를 탐색하는 경우와, 탐색하지 않는 경우로 나눠서 모든 경우를 탐색하는 재귀탐색 이다.
