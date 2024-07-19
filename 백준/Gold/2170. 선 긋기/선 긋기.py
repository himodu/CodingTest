n = int(input())

lines = []

for i in range(n):
    s,e = map(int, input().split())
    lines.append((s,e))

lines.sort()

long = lines[0][1] - lines[0][0]
end = lines[0][1]

for i in range(1,n):
    if end >= lines[i][0]:
        if lines[i][1] <= end:
            continue
        long += lines[i][1] - end
        end = lines[i][1]
    else:
        long += lines[i][1]-lines[i][0]
        end = lines[i][1]

print(long)