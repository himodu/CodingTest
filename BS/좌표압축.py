n = int(input())

input = list(map(int, input().split()))

origin = input.copy()
data = list(set(input))
data.sort()

def bs(find):
    start = 0
    end = len(data)-1
    result = 0
    while start <= end:
        index = (start+end)//2

        if data[index] < find:
            start = index+1
        else:
            if data[index] == find:
                result = index
            end = index-1
    return result

result = []
for i in origin:
    result.append(bs(i))

print(*result)
