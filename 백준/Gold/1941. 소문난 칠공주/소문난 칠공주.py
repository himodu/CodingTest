from collections import deque
from itertools import combinations

set = [input() for i in range(5)]

visited = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

combi = []
result = 0

def bfs():
    length = 0
    count = 0
    visited = [False]*7

    queue = deque()
    queue.append(combi[0])
    visited[0] = True
    while queue:
        x, y = queue.popleft()
        length += 1
        if set[x][y] == 'S':
            count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            for j in range(7):
                cx, cy = combi[j]
                if nx==cx and ny==cy and not visited[j]:
                    queue.append((nx,ny))
                    visited[j] = True
                else:
                    continue

    if count>=4 and length==7:
        return True
    else:
        return False

points = []
for i in range(5):
    for j in range(5):
        points.append((i,j))

for comb in combinations(points, 7):
    combi = list(comb).copy()
    if bfs():
        result += 1


# def com(index, length):
#     global result
#
#     if index==24:
#         if length==7 and bfs():
#             result += 1
#         return
#
#     if length==7 and bfs():
#         result += 1
#         return
#
#     for i in range(index, 25):
#         combi.append(points[i])
#         com(i+1, length+1)
#         combi.pop()
#
#
# com(0,0)
print(result)