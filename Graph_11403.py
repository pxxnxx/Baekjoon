import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list()
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    check = [0 for _ in range(n)]
    queue = deque([i])
    while queue:
        x = queue.popleft()
        for j in range(n):
            if arr[x][j] == 1 and check[j] != 1:
                queue.append(j)
                check[j] = 1
                arr[i][j] = 1
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()
