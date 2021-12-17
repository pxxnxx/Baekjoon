import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int,input().split())
dist = [[sys.maxsize for _ in range(n)] for _ in range(n)]
arr = [[_+1 for _ in range(n)] for _ in range(n)]
for i in range(m):
    s, e, v = map(int,input().split())
    dist[s-1][e-1] = v
    dist[e-1][s-1] = v
for k in range(n):
    dist[k][k] = 0
    arr[k][k] = '-'
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                arr[i][j] = arr[i][k]
for i in range(n):
    print(*arr[i])