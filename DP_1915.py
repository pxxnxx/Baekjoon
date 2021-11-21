import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = []
dp = [[0 for _ in range(m)] for _ in range(n)]
answer = 0
for i in range(n):
    arr.append(list(map(int,input().strip())))
    for j in range(m):
        if arr[i][j] == 1:
            dp[i][j] = 1

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])
        if arr[i][j] == 1:
            dp[i][j] += 1
        else:
            dp[i][j] = 0

for i in range(n):
    if answer < max(dp[i]):
        answer = max(dp[i])
print(answer*answer)
# FAILED




# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr = []
# dp = [[0 for _ in range(m)] for _ in range(n)]
# answer = 0
# # arr = [[1 for _ in range(200)] for _ in range(200)]
# for i in range(n):
#     arr.append(list(map(int, input().strip())))
#
#     for j in range(m):
#         if arr[i][j] == 1:
#             dp[i][j] = 1
#             answer = 1
#
# def square(y, x, v):
#     for i in range(y+v, y-1, -1):
#         if arr[i][x+v] == 0:
#             return v
#     for i in range(x+v, x-1, -1):
#         if arr[y+v][i] == 0:
#             return v
#     return v+1
# update = 0
#
# for k in range(1, min(n, m)+1-answer):
#     if k > answer:
#         break
#     for i in range(n-answer):
#         for j in range(m-answer):
#             if dp[i][j] == answer:
#                 dp[i][j] = square(i, j, dp[i][j])
#                 if dp[i][j] > answer:
#                     update = 1
#                 #     answer = dp[i][j]
#     if update == 1:
#         answer += 1
#         update = 0
# # for i in range(n):
# #     print(dp[i])
#
# print(answer**2)