n = int(input())

posper = []
negper = []

for i in range(n):
    e = int(input())
    if e > 0:
        posper.append(e)
    else:
        negper.append(e)

posper.sort(reverse=True)
negper.sort()

result = 0
i = 0
next = 0
n = len(posper)
while True:
    i = next
    if i >= n-1:
        if i==n-1:
            result += posper[i]
        break

    if posper[i+1] > 1:
        result += posper[i]*posper[i+1]
        next += 2

    if posper[i+1] == 1:
        result += posper[i]
        next += 1

i = 0
next = 0
n = len(negper)
while True:
    i = next
    if i >= n-1:
        if i==n-1:
            result += negper[i]
        break

    result += negper[i]*negper[i+1]
    next += 2

print(result)

# 이 문제를 통해 Greedy 에 대한 깨달음을 얻었음 
# 결국에 Greedy는 풀이법을 떠올리기 쉽지 않을 수 있지만 정렬을 통해서 지금 다루는 값이 항상 최적의 값이라는 것을 보장하는 것이 핵심이다.
