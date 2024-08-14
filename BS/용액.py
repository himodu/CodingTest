n = int(input())

data = list(map(int, input().split()))

data.sort()

def bs(find):
    start = 0
    end = n-1
    minmix = 1e10
    result = 0
    while start <= end:
        mid = (start+end)//2
        mix = find+data[mid]
        if abs(mix) < minmix and data[mid] != find:
            minmix = abs(mix)
            result = mid
        if mix >= 0:
            end = mid-1
        else:
            start = mid+1
    return result

fir = 0
sec = 0
mix = 1e10
for i in range(n):
    find = bs(data[i])
    if abs(data[i]+data[find]) <= mix:
        mix = abs(data[i]+data[find])
        if data[i] > data[find]:
            fir = data[find]
            sec = data[i]
        else:
            fir = data[i]
            sec = data[find]

print(fir, sec)