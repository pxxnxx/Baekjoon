import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, r = map(int,input().split())
    mirror = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(r):
        my, mx = map(int,input().split())
        mirror[my-1][mx-1] = 1
    y, x = map(int,input().split())
    y -= 1
    x -= 1
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    if y == n:
        v = 0
    elif x == -1:
        v = 1
    elif y == -1:
        v = 2
    else:
        v = 3
    y += dy[v]
    x += dx[v]
    while 0 <= y < n and 0 <= x < n:
        if mirror[y][x] == 1:
            v = (v+1)%4
        y += dy[v]
        x += dx[v]
    print(y+1, x+1)