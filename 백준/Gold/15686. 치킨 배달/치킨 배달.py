n,m = map(int, input().split())

field = []

for i in range(n):
    field.append(list(map(int, input().split())))

chickens = []
houses = []

for i in range(n):
    for j in range(n):
        if field[i][j]==1:
            houses.append((i,j))
        elif field[i][j]==2:
            chickens.append((i,j))



def distance(combi):
    global houses
    distance = 0
    for hx, hy in houses:
        minDis = 10e9
        for cx, cy in combi:
            if minDis > abs(cx - hx) + abs(cy - hy):
                minDis = abs(cx - hx) + abs(cy - hy)

        distance += minDis

    return distance

com = []
min = 10e9


def combi(index):
    global min

    if len(com)==m:
        candi = distance(com)
        if candi<min:
            min = candi
        return

    if index==len(chickens):
        if len(com)==m:
            candi = distance(com)
            if candi<min:
                min = candi
        return

    com.append(chickens[index])
    combi(index+1)
    com.pop()
    combi(index+1)


combi(0)
print(min)