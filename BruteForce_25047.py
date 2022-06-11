import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

answer = -sys.maxsize
def choice(que, ind, val, lim):
    global answer
    if val == lim:
        s = 0
        row = [0] * n
        col = [0] * n
        for y in que:
            s += sum(arr[y])
        for i in range(n):
            for j in range(n):
                if i in que:
                    col[j] += arr[i][j]
                else:
                    col[j] -= arr[i][j]
        col.sort(reverse=True)
        for i in range(n):
            if col[i] <= 0:
                break
            s -= col[i]
        answer = max(answer, s)
        choice(que, ind, val, lim+1)
        return

    for i in range(ind+1, n):
        que.append(i)
        choice(que, i, val+1, lim)
        que.pop()

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
choice([], -1, 0, 0)
print(answer)