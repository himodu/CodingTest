from  collections import deque

s, e=map(int, input().split())

field = [-1]*100001

def bfs(start):
    queue = deque()
    queue.append(start)
    field[start] = 0
    while queue:
        current = queue.popleft()
        if current==e:
            break
        for i in range(3):
            if i == 0:
                if current==0:
                    continue
                next = current*2
            if i == 1:
                next = current-1
            if i == 2:
                next = current+1

            if next <= -1 or next >= 100001:
                continue

            if field[next]==-1:
                if not i==0:
                    field[next] = field[current]+1
                    queue.append(next)
                else:
                    field[next] = field[current]
                    queue.appendleft(next)

bfs(s)
print(field[e])