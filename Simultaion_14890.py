import sys
input = sys.stdin.readline
n, l = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = 0
for i in range(n):
    rw = [0 for _ in range(n)]
    start = arr[i][0]
    a = 0
    for j in range(n):
        if start > arr[i][j]:
            if start != arr[i][j] + 1:
                a = 1
                break
            if j + l - 1 >= n:
                a = 1
                break
            b = 0
            for k in range(l):
                if arr[i][j] != arr[i][j+k] or rw[j+k] != 0:
                    b = 1
                    break
            if b == 1:
                a = 1
                break
            start = arr[i][j]
            for k in range(l):
                rw[j+k] = 1
        elif start < arr[i][j]:
            if start != arr[i][j] - 1:
                a = 1
                break
            if j - l < 0:
                a = 1
                break
            b = 0
            for k in range(l):
                if arr[i][j-1] != arr[i][j-1-k] or rw[j-1-k] != 0:
                    b = 1
                    break
            if b == 1:
                a = 1
                break
            start = arr[i][j]
            for k in range(l):
                rw[j-1-k] = 1
    if a == 0:
        answer += 1
for j in range(n):
    rw = [0 for _ in range(n)]
    start = arr[0][j]
    a = 0
    for i in range(n):
        if start > arr[i][j]:
            if start != arr[i][j] + 1:
                a = 1
                break
            if i + l - 1 >= n:
                a = 1
                break
            b = 0
            for k in range(l):
                if arr[i][j] != arr[i+k][j] or rw[i+k] != 0:
                    b = 1
                    break
            if b == 1:
                a = 1
                break
            start = arr[i][j]
            for k in range(l):
                rw[i+k] = 1
        elif start < arr[i][j]:
            if start != arr[i][j] - 1:
                a = 1
                break
            if i - l < 0:
                a = 1
                break
            b = 0
            for k in range(l):
                if arr[i-1][j] != arr[i-1-k][j] or rw[i-1-k] != 0:
                    b = 1
                    break
            if b == 1:
                a = 1
                break
            start = arr[i][j]
            for k in range(l):
                rw[i-1-k] = 1
    if a == 0:
        answer += 1
print(answer)

