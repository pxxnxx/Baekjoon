import sys

ap = -sys.maxsize
an = sys.maxsize

def DFS(y,x,p):
    global ap, an

    if y == n-1 and x == n-1:
        ap = max(ap,p)
        an = min(an,p)
        return

    for i in range(2):
        yy, xx = y + dy[i], x + dx[i]
        if yy == n or xx == n:
            continue
        if arr[y][x] == '*':
            DFS(yy,xx,p*arr[yy][xx])
        elif arr[y][x] == '+':
            DFS(yy,xx,p+arr[yy][xx])
        elif arr[y][x] == '-':
            DFS(yy,xx,p-arr[yy][xx])
        else:
            DFS(yy,xx,p)

n = int(input())
arr = [list(map(str,input().split())) for _ in range(n)]
dy = [0, 1]
dx = [1, 0]
for i in range(n):
    for j in range(n):
        if (i+j)%2 == 0:
            arr[i][j] = int(arr[i][j])
DFS(0,0,arr[0][0])
print(ap,an)

# import sys
#
# answerp = -sys.maxsize
# answerm = sys.maxsize
# def Backp(y, x, p):
#     global answerp
#     if y == n-1 and x == n-1:
#         print(p)
#         answerp = max(answerp, p)
#         return
#     if arr[y][x] == '*':
#         if y+1 < n and visitp[y+1][x] < p * arr[y+1][x]:
#             visitp[y+1][x] = p * arr[y+1][x]
#             Backp(y+1, x, p * arr[y+1][x])
#         if x+1 < n and visitp[y][x+1] < p * arr[y][x+1]:
#             visitp[y][x+1] = p * arr[y][x+1]
#             Backp(y, x+1, p * arr[y][x+1])
#     if arr[y][x] == '+':
#         if y+1 < n and visitp[y+1][x] < p + arr[y+1][x]:
#             visitp[y+1][x] = p + arr[y+1][x]
#             Backp(y+1, x, p + arr[y+1][x])
#         if x+1 < n and visitp[y][x+1] < p + arr[y][x+1]:
#             visitp[y][x+1] = p + arr[y][x+1]
#             Backp(y, x+1, p + arr[y][x+1])
#     if arr[y][x] == '-':
#         if y+1 < n and visitp[y+1][x] < p - arr[y+1][x]:
#             visitp[y+1][x] = p - arr[y+1][x]
#             Backp(y+1, x, p - arr[y+1][x])
#         if x+1 < n and visitp[y][x+1] < p - arr[y][x+1]:
#             visitp[y][x+1] = p - arr[y][x+1]
#             Backp(y, x+1, p - arr[y][x+1])
#     else:
#         if y+1 < n:
#             Backp(y+1, x, p)
#         if x+1 < n:
#             Backp(y, x+1, p)
#
# def Backm(y, x, m):
#     global answerm
#     if y == n-1 and x == n-1:
#         answerm = min(answerm, m)
#         return
#     if arr[y][x] == '*':
#         if y+1 < n and visitm[y+1][x] > m * arr[y+1][x]:
#             visitm[y+1][x] = m * arr[y+1][x]
#             Backm(y+1, x, m * arr[y+1][x])
#         if x+1 < n and visitm[y][x+1] > m * arr[y][x+1]:
#             visitm[y][x+1] = m * arr[y][x+1]
#             Backm(y, x+1, m * arr[y][x+1])
#     elif arr[y][x] == '+':
#         if y+1 < n and visitm[y+1][x] > m + arr[y+1][x]:
#             visitm[y+1][x] = m + arr[y+1][x]
#             Backm(y+1, x, m + arr[y+1][x])
#         if x+1 < n and visitm[y][x+1] > m + arr[y][x+1]:
#             visitm[y][x+1] = m + arr[y][x+1]
#             Backm(y, x+1, m + arr[y][x+1])
#     elif arr[y][x] == '-':
#         if y+1 < n and visitm[y+1][x] > m - arr[y+1][x]:
#             visitm[y+1][x] = m - arr[y+1][x]
#             Backm(y+1, x, m - arr[y+1][x])
#         if x+1 < n and visitm[y][x+1] > m - arr[y][x+1]:
#             visitm[y][x+1] = m - arr[y][x+1]
#             Backm(y, x+1, m - arr[y][x+1])
#     else:
#         if y+1 < n:
#             Backm(y+1, x, m)
#         if x+1 < n:
#             Backm(y, x+1, m)
#
# n = int(input())
# arr = [list(map(str,input().split())) for _ in range(n)]
# visitp = [[-sys.maxsize for _ in range(n)] for _ in range(n)]
# visitm = [[sys.maxsize for _ in range(n)] for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if (i+j) % 2 == 0:
#             arr[i][j] = int(arr[i][j])
# Backp(0, 0, arr[0][0])
# Backm(0, 0, arr[0][0])
# print(answerp, answerm)