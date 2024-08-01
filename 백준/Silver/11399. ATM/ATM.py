n = int(input())

list = list(map(int, input().split()))

list.sort()
temp = 0
result = 0

for i in range(n):
    temp += list[i]
    result += temp

print(result)