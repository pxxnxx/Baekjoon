import sys
t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    end = 0
    for j in range(n):
        arr.append(sys.stdin.readline().strip())
    arr = sorted(arr)
    for k in range(n-1):
        j = 0
        while j < len(arr[k]) and j < len(arr[k+1]):
            if arr[k][j] != arr[k+1][j]:
                break
            j += 1
        if j == len(arr[k]) or j == len(arr[k+1]):
            print("NO")
            end = 1
            break
    if end == 0:
        print("YES")

