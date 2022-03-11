def Check(y, x, q):
    visit[y][x] = 1
    q.append([y, x])
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < 12 and 0 <= xx < 6 and visit[yy][xx] == 0 and arr[yy][xx] == arr[y][x]:
            Check(yy, xx, q)

def Pop():
    p = 0
    for i in Puyo:
        for j in Puyo[i]:
            if len(j) < 4:
                continue
            for yy, xx in j:
                arr[yy][xx] = '.'
            p = 1
        Puyo[i] = []
    return p

def Gravity(y, x):
    for yy in range(y-1, -1, -1):
        if arr[yy][x] != '.':
            arr[y][x] = arr[yy][x]
            arr[yy][x] = '.'
            return 1
    return 0

arr = [list(map(str,input())) for _ in range(12)]
Puyo = {'R' : [], 'G' : [], 'B' : [], 'P' : [], 'Y' : []}

dy = [0,1,0,-1]
dx = [1,0,-1,0]
answer = 0
while True:
    visit = [[0 for _ in range(6)] for _ in range(12)]
    for j in range(6):
        for i in range(11, -1, -1):
            if arr[i][j] == '.':
                break
            if visit[i][j] == 0:
                temp = []
                Check(i, j, temp)
                Puyo[arr[i][j]].append(temp)
    if not Pop():
        break
    answer += 1
    for j in range(6):
        for i in range(11, -1, -1):
            if arr[i][j] == '.':
                if not Gravity(i, j):
                    break
print(answer)