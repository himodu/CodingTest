import heapq

n = int(input())

heap = []
for i in range(n):
    s, e= map(int, input().split())
    heapq.heappush(heap, (e, s))

count = 0
prev = 0
while heap:
    ce,cs = heapq.heappop(heap)
    if prev <= cs:
        count += 1
        prev = ce

print(count)


