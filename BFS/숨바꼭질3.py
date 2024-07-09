from  collections import deque

s, e=map(int, input().split())

field = [-1]*100001

def bfs(start):
    queue = deque()
    queue.append(start)
    field[start] = 0
    while queue:
        current = queue.popleft()
        for i in range(3):
            if i == 0:
                if current==0:
                    continue
                next = current*2
            if i == 1:
                next = current+1
            if i == 2:
                next = current-1

            if next <= -1 or next >= 100001:
                continue

            if field[next]==-1:
                if not i==0:
                    field[next] = field[current]+1
                    queue.append(next)
                else:
                    field[next] = field[current]
                    queue.append(next)
            else:
                if not i==0:
                    if field[next] > field[current]+1:
                        field[next] = field[current]+1
                        queue.append(next)
                else:
                    if field[next] > field[current]:
                        field[next] = field[current]
                        queue.append(next)

bfs(s)
print(field[e])

# 이 문제는 BFS 의 경우 방문 체크만 해줬을 때 항상 최적의 경로를 탐색하는 것은 아니라는 것을 알게 해준 문제 
# appendleft 로 강제로 큐의 맨 앞에 강제로 집어 넣거나 값을 저장하고, 경로를 찾을 때마다 최솟값 비교를 통해 최적의 답을 동적으로 저장해주면 된다.
