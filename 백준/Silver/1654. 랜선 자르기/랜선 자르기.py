k, n = map(int, input().split())

lines = []

max = 0
for i in range(k):
    line = int(input())
    lines.append(line)
    if line > max:
        max = line

start = 1
end = max

result = 0

while end >= start:
    count = 0
    index = (start + end) // 2

    for i in range(k):
        able = lines[i] // index
        count += able

    if count < n:
        end = index-1
    else:
        result = index
        start = index+1


print(result)