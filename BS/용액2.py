n = int(input())

data = list(map(int, input().split()))
data.sort()

start = 0
end = n-1
min = 1e10
fir = 0
sec = 0
while start<end:
    if start > n-1 or end < 0:
        break
    if abs(data[start] + data[end]) <= min:
        min = abs(data[start]+data[end])
        fir = start
        sec = end
    if abs(data[start+1]+data[end]) > abs(data[start]+data[end-1]):
        end -= 1
    else:
        start += 1

print(data[fir], data[sec])
