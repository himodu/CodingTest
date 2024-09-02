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

# 이 문제는 백트래킹 문제의 기본문제라고 하는데 난 뒤지게 어려웠다...
# 2차원 배열이니까 2차원배열으로 접근하려고 했는데 너무 어려워져서...
# 해당 문제에서는 row를 탐색 기준으로 잡고, 어차피 한 row에는 하나의 queen 만 놓을 수 있으니 queen 의 위치를 옆으로 옮겨가면서 진행
# row를 +1 씩 진행시키면서 즉 밑으로 내려가면서 위에 있는 row에 놓여져있는 퀸의 위치를 가져와서 놓을 수 있는 지 판단한 다음에 가능하면
# 탐색을 진행하면 된다. 따로 방문처리를 할 필요는 없다.
