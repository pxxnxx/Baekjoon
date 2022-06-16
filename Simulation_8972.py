import sys
input = sys.stdin.readline

def crazy(q):
    nq = []
    same = []
    nm = [['.' for _ in range(n)] for _ in range(m)]
    for ry, rx in q:
        # 로봇 이동
        v = [y-ry, x-rx]
        if v[0] > 0:
            v[0] = 1
        elif v[0] < 0:
            v[0] = -1
        if v[1] > 0:
            v[1] = 1
        elif v[1] < 0:
            v[1] = -1
        ny = ry + v[0]
        nx = rx + v[1]
        # 만날 시 종료
        if arr[ny][nx] == 'I':
            return -1
        # 같은 경우 체크용 배열에만 저장
        elif nm[ny][nx] == 'R':
            same.append([ny,nx])
        # 다음 배열에 저장한 후 시간을 줄이기 위해 2차원 배열에 R 위치 저장
        else:
            nq.append([ny,nx])
            nm[ny][nx] = 'R'

    # return 배열에 살아 있는 로봇만 저장
    rnq = []
    for xq in nq:
        if xq not in same:
            rnq.append(xq)

    return rnq

n, m = map(int,input().split())
arr = [list(str(input().strip())) for _ in range(n)]
move = list(map(int,input().strip()))
dy = [0,1,1,1,0,0,0,-1,-1,-1]
dx = [0,-1,0,1,-1,0,1,-1,0,1]
robot = []
y, x = 0, 0
# 위치 체크
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            y, x = i, j
        elif arr[i][j] == 'R':
            robot.append([i, j])
answer = 0
for v in move:
    # 종수 이동
    yy = y + dy[v]
    xx = x + dx[v]
    answer += 1
    if yy == y and xx == x:
        pass
    # 폭발
    elif arr[yy][xx] == 'R':
        print("kraj",answer)
        answer = -1
        break
    else:
        arr[yy][xx] = 'I'
        arr[y][x] = '.'
        y, x = yy, xx
    after = crazy(robot)
    # 폭발
    if after == -1:
        print("kraj",answer)
        answer = -1
        break
    # 배열 변경
    else:
        for ry, rx in robot:
            arr[ry][rx] = '.'
        for ry, rx in after:
            arr[ry][rx] = 'R'
        robot = after
if answer != -1:
    for i in range(n):
        print(*arr[i],sep='')