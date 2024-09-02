n,s = map(int, input().split())

list = list(map(int, input().split()))

sum = 0

for i in range(n):
    sum += list[i]

def search():
    start = 0
    end = 0
    sum = 0
    min_length = 1e9

    while start <= end:

        if sum >= s:
            min_length = min(min_length, end-start)
            sum -= list[start]
            start += 1
        else:
            if end == n:
                break
            sum += list[end]
            end += 1

    return min_length

if sum < s:
    print(0)
else:
    print(search())

