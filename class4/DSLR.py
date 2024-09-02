from collections import deque

n = int(input())
case = []

for i in range(n):
    c1, c2 = map(int, input().split())
    case.append((c1,c2))

def D(num):
    num *= 2
    if num > 9999:
        return (num)%10000
    else:
        return num
def S(num):
    if num==0:
        return 9999
    else:
        return num-1
def L(num):
    fir = num//1000
    num *= 10
    num += fir
    num = num % 10000
    return num
def R(num):
    fin = num%10
    num //= 10
    num += fin*1000
    return num

def bfs(start, end):
    visited = [False] * 10001
    queue = deque()
    queue.append((start, ''))

    while queue:
        index, route = queue.popleft()

        if index==end:
            return route

        nindex = D(index)
        if not visited[nindex]:
            visited[nindex] = True
            queue.append((nindex, route+'D'))

        nindex = S(index)
        if not visited[nindex]:
            visited[nindex] = True
            queue.append((nindex, route+'S'))

        nindex = L(index)
        if not visited[nindex]:
            visited[nindex] = True
            queue.append((nindex, route+'L'))

        nindex = R(index)
        if not visited[nindex]:
            visited[nindex] = True
            queue.append((nindex, route+'R'))

for i in range(n):
    n1, n2 = case[i]
    route = bfs(n1,n2)
    print(route)