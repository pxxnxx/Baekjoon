import sys
n,m = map(int,sys.stdin.readline().split())
arr = [int(x) for x in sys.stdin.readline().split()]

start, end = 0, max(arr)
while start <= end:
    mid = (start + end) // 2
    tree = 0
    for i in arr:
        if i - mid > 0:
            tree += i - mid
    if tree == m:
        end = mid
        break
    elif tree < m:
        end = mid - 1
    else:
        start = mid + 1
print(end)
