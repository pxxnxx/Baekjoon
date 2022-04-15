import sys
sys.setrecursionlimit(1000001)
input = sys.stdin.readline

dy = [0,1,0,-1]
dx = [1,0,-1,0]
case = 1

def Back(y, x, vec, check, ret):
    global answer
    if check == total and answer > ret:
        answer = ret
        return
    next_y = y + dy[vec]
    next_x = x + dx[vec]
    queue = []
    tf = 0
    while 0 <= next_y < n and 0 <= next_x < m and arr[next_y][next_x] == '.':
        tf = 1
        queue.append([next_y, next_x])
        arr[next_y][next_x] = 'X'
        arr[y][x] = 'v'
        check += 1
        y = next_y
        x = next_x
        next_y = y + dy[vec]
        next_x = x + dx[vec]
    if tf == 0:
        return
    ret += 1
    if check == total and answer > ret:
        answer = ret

        for a, b in queue:
            arr[a][b] = '.'
            return
    if answer < ret:
        for a, b in queue:
            arr[a][b] = '.'
            return

    for k in range(1,4,2):
        nv = (vec+k)%4
        ny = y + dy[nv]
        nx = x + dx[nv]
        if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == '.':
            Back(y, x, nv, check, ret)
    for a, b in queue:
        arr[a][b] = '.'

while True:
    try:
        n, m = map(int,input().split())
        arr = [list(str(input().strip())) for _ in range(n)]
        answer = sys.maxsize
        total = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == '.':
                    total += 1
        for i in range(n):
            for j in range(m):
                if arr[i][j] != '.':
                    continue
                for k in range(4):
                    arr[i][j] = 'v'
                    Back(i, j, k, 1, 0)
                    for a in range(n):
                        for b in range(m):
                            if arr[a][b] == '*':
                                continue
                            arr[a][b] = '.'

        if answer == sys.maxsize:
            answer = -1
        print("Case ", case, ": ", answer ,sep='')
        case += 1

    except:
        break
