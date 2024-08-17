l, c = map(int, input().split())

chars = list(input().split())
chars.sort()

answer = []

def ismot(chars):
    mot = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in range(len(chars)):
        for j in range(len(mot)):
            if chars[i]==mot[j]:
                count += 1
    return count

def track(index):

    length = len(answer)
    mot = ismot(answer)
    if index == c:
        if length == l and mot >= 1 and length-mot >= 2:
            for i in range(length):
                print(answer[i], end='')
            print()
        return

    if length == l and mot >= 1 and length-mot >= 2:
        for i in range(length):
            print(answer[i], end='')
        print()
        return

    answer.append(chars[index])
    track(index+1)

    answer.pop()
    track(index+1)

track(0)