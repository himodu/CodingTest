n = int(input())

data = list(map(int, input().split()))

data.sort()
result = 0

def search(find, index):
    start = 0
    end = n-1

    while start < end:
        if start == index:
            start += 1
            continue
        if end == index:
            end -= 1
            continue
        cand = data[start] + data[end]
        if cand == find:
            return True
        if cand > find:
            end -= 1
        else:
            start += 1
    return False

for i in range(n):
    if search(data[i], i):
        result += 1

print(result)