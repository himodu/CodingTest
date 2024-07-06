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