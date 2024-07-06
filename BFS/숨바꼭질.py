from collections import deque

n,k=map(int, input().split())

field = [0] * 100001

def bfs(n,k):
    queue = deque()
    queue.append(n)
    while queue:
        n = queue.popleft()
        if n == k:
            break
        for i in range(3):
            if i==0:
                nn = n*2
                if nn==0:
                    continue
            if i==1:
                nn = n + 1
            if i==2:
                nn = n - 1
            if nn <= -1 or nn >= 100001:
                continue
            if field[nn]==0:
                field[nn] = field[n] + 1
                queue.append(nn)

bfs(n,k)
print(field[k])

# 이 문제는 BFS에 대한 통찰을 아주 맛있게 얻을 수 있게 해준 문제
# BFS는 방문처리 + 목적지 설정(최적화)만 해준다면 항상 최적의 탐색을 해낼 수 있다.
# 방문처리를 해주었기 때문에 항상 효율적인 선택만 한다는 것이다 (Cycle 제거)