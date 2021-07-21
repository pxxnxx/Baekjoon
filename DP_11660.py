import sys
input = sys.stdin.readline
arr = list()
n,m = map(int,input().split())
for i in range(n):
    arr.append(list(map(int,input().split())))
    if i != 0:
        for j in range(n):
            arr[i][j] += arr[i-1][j]
for i in range(m):
    xa, ya, xb, yb = map(int,input().split())
    s = 0
    for j in range(ya-1,yb):
        if xa == 1:
            s += arr[xb-1][j]
        else:
            s += arr[xb-1][j] - arr[xa-2][j]
    print(s)
