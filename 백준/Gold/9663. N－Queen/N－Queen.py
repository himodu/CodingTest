n = int(input())

row = [0]*n

result = 0

def isAble(rowNum):
    for i in range(rowNum):
        if row[i]==row[rowNum] or rowNum-i == abs(row[i]-row[rowNum]):
            return False
    return True

def track(rowNum):
    global result
    if rowNum==n:
        result += 1
        return
    for i in range(n):
        row[rowNum] = i
        if isAble(rowNum):
            track(rowNum+1)

track(0)
print(result)