n1, n2 = map(int, input().split())

lis = []
see = []

for i in range(n1):
    lis.append(input())

for i in range(n2):
    see.append(input())


p1 = 0
p2 = 0

lis.sort()
see.sort()

result = []

while p1 < n1 and p2 < n2:
    if lis[p1] == see[p2]:
        result.append(lis[p1])
        p1 += 1
        p2 += 1
    elif lis[p1] > see[p2]:
        p2 += 1
    else:
        p1 += 1

print(len(result))
for i in range(len(result)):
    print(result[i])