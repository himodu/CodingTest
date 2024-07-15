n = int(input())

lofes = []
for i in range(n):
    lofes.append(int(input()))

lofes.sort()

result = 0
for i in range(n):
    if result < (n-i)*lofes[i]:
        result = (n-i)*lofes[i];

print(result)