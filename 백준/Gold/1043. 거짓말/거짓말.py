n,m = map(int, input().split())

tr = list(map(int, input().split()))

link = [i for i in range(n+1)]

inputSave = []

for i in range(m):

    inputList = list(map(int, input().split()))
    inputSave.append(inputList)

    cnt = inputList[0]

    root = link[inputList[1]]
    for j in range(1, cnt+1):
        candi = inputList[j]
        preRoot = link[candi]
        for k in range(n+1):
            if link[k] == preRoot:
                link[k] = root

result = 0
for inp in inputSave:

    cnt = inp[0]
    isPoss = True

    for j in range(1, cnt+1):
        candi = inp[j]
        for k in range(1, tr[0]+1):
            if candi == tr[k] or link[candi] == link[tr[k]]:
                isPoss = False

    if isPoss:
        result += 1

print(result)