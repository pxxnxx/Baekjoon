import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

def bfs():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < n and 0 <= xx < m:
                if yy == n-1 and xx == m-1:
                    print(vst[y][x]+1)
                    return
                if arr[yy][xx] == 1:
                    if brk[yy][xx] <= brk[y][x]+1 and vst[yy][xx] <= vst[y][x]+1:
                        continue
                    if brk[y][x]+1 > k:
                        continue
                    vst[yy][xx] = vst[y][x]+1
                    brk[yy][xx] = brk[y][x]+1
                    queue.append([yy, xx])

                else:
                    if brk[yy][xx] <= brk[y][x] and vst[yy][xx] <= vst[y][x]+1:
                        continue
                    vst[yy][xx] = vst[y][x]+1
                    brk[yy][xx] = brk[y][x]
                    queue.append([yy, xx])
    print(-1)

n, m, k = map(int,input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
vst = [[sys.maxsize for _ in range(m)] for _ in range(n)]
brk = [[0 for _ in range(m)] for _ in range(n)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
queue = deque([[0, 0]])
vst[0][0] = 1
if n == 1 and m == 1:
    print(1)
else:
    bfs()



# import sys
# sys.stdin = open("input.txt")
# input = sys.stdin.readline
# answer = sys.maxsize
# test = 0
# def DFS(y, x):
#     global answer
#     global test
#     test += 1
#     print(test)
#     if y+1 == n and x+1 == m:
#         answer = min(answer, vst[y][x])
#         return
#     for i in range(4):
#         yy = y + dy[i]
#         xx = x + dx[i]
#         if 0 <= yy < n and 0 <= xx < m:
#             print(yy,xx)
#             if arr[yy][xx] == 1:
#                 if brk[yy][xx] <= brk[y][x]+1 and vst[yy][xx] <= vst[y][x] + 1:
#                     continue
#                 vst[yy][xx] = vst[y][x] + 1
#                 brk[yy][xx] = brk[y][x] + 1
#                 DFS(yy,xx)
#             else:
#                 if brk[yy][xx] <= brk[y][x] and vst[yy][xx] <= vst[y][x] + 1:
#                     continue
#                 vst[yy][xx] = vst[y][x] + 1
#                 brk[yy][xx] = brk[y][x]
#                 DFS(yy,xx)
#             # if arr[yy][xx] == 0:
#             #     vst[yy][xx] = vst[y][x]+1
#             #     brk[yy][xx] = brk[y][x]
#             #     DFS(yy,xx,vst,brk)
#             # elif arr[yy][xx] == 1 and brk[y][x] < k:
#             #     vst[yy][xx] = vst[y][x]+1
#             #     brk[yy][xx] = brk[y][x]+1
#             #     DFS(yy,xx,vst,brk)
#             # vst[yy][xx] = 0
#             # brk[yy][xx] = 0
#
#
# import time
# start = time.time()
# n, m, k = map(int,input().split())
# arr = [list(map(int,input().strip())) for _ in range(n)]
# vst = [[sys.maxsize for _ in range(m)] for _ in range(n)]
# brk = [[0 for _ in range(m)] for _ in range(n)]
# dy = [0, 1, 0, -1]
# dx = [1, 0, -1, 0]
# vst[0][0] = 1
# print("1")
# DFS(0,0)
# if answer == sys.maxsize:
#     answer = -1
# print(answer)
# print(time.time()-start)