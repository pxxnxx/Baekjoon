from collections import deque

def cti(c):
    return ord(c.lower())-97

def clear():
    for i in range(n):
        for j in range(m):
            visit[i][j] = 0

def add_start():
    global answer
    for i in range(m):
        if arr[0][i] == '.':
            start.add((0,i))
        if arr[n-1][i] == '.':
            start.add((n-1,i))
        if 'a' <= arr[0][i] <= 'z':
            start.add((0,i))
            key[cti(arr[0][i])] = 1
            arr[0][i] = '.'
        if 'a' <= arr[n-1][i] <= 'z':
            start.add((n-1,i))
            key[cti(arr[n-1][i])] = 1
            arr[n-1][i] = '.'
        if 'A' <= arr[0][i] <= 'Z' and key[cti(arr[0][i])] == 1:
            start.add((0,i))
            arr[0][i] = '.'
        if 'A' <= arr[n-1][i] <= 'Z' and key[cti(arr[n-1][i])] == 1:
            start.add((n-1,i))
            arr[n-1][i] = '.'
        if arr[0][i] == '$':
            start.add((0,i))
            arr[0][i] = '.'
            answer += 1
        if arr[n-1][i] == '$':
            start.add((n-1,i))
            arr[n-1][i] = '.'
            answer += 1
    for i in range(1,n-1):
        if arr[i][0] == '.':
            start.add((i,0))
        if arr[i][m-1] == '.':
            start.add((i,m-1))
        if 'a' <= arr[i][0] <= 'z':
            start.add((i,0))
            key[cti(arr[i][0])] = 1
            arr[i][0] = '.'
        if 'a' <= arr[i][m-1] <= 'z':
            start.add((i,m-1))
            key[cti(arr[i][m-1])] = 1
            arr[i][m-1] = '.'
        if 'A' <= arr[i][0] <= 'Z' and key[cti(arr[i][0])] == 1:
            start.add((i,0))
            arr[i][0] = '.'
        if 'A' <= arr[i][m-1] <= 'Z' and key[cti(arr[i][m-1])] == 1:
            start.add((i,m-1))
            arr[i][m-1] = '.'
        if arr[i][0] == '$':
            start.add((i,0))
            arr[i][0] = '.'
            answer += 1
        if arr[i][m-1] == '$':
            start.add((i,m-1))
            arr[i][m-1] = '.'
            answer += 1

def BFS(fy,fx):
    global answer
    global changed

    queue = deque([[fy, fx]])
    visit[fy][fx] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < n and 0 <= xx < m and visit[yy][xx] == 0:
                if arr[yy][xx] == '*':
                    continue
                elif arr[yy][xx] == '.':
                    queue.append([yy,xx])
                    visit[yy][xx] = 1
                elif arr[yy][xx] == '$':
                    queue.append([yy,xx])
                    visit[yy][xx] = 1
                    arr[yy][xx] = '.'
                    answer += 1
                elif 'a' <= arr[yy][xx] <= 'z':
                    key[cti(arr[yy][xx])] = 1
                    arr[yy][xx] = '.'
                    changed = 1
                    visit[yy][xx] = 1
                elif key[cti(arr[yy][xx])] == 1:
                    queue.append([yy,xx])
                    changed = 1
                    visit[yy][xx] = 1
                    arr[yy][xx] = '.'




# TODO
#   1. 시작점 찾기
#   2. BFS로 변동사항 찾기
#   3. 변동사항 생기면 visit 초기화

for _ in range(int(input())):
    answer = 0
    changed = 1

    # Setting
    n, m = map(int,input().split())
    arr = [list(str(input())) for _ in range(n)]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    key = [0] * 26
    dy = [0,-1,0,1]
    dx = [1,0,-1,0]
    start = set()

    k = input()
    for x in k:
        if x == '0':
            break
        key[cti(x)] = 1

    test = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '$':
                test += 1

    while changed:
        changed = 0
        clear()
        add_start()
        for y, x in start:
            BFS(y,x)
    print(answer)
