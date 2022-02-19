import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
l, r = 0, n-1
m = sys.maxsize
while l < r:
    s = arr[l] + arr[r]
    if m > abs(s):
        answer = [arr[l], arr[r]]
        m = abs(s)
    if s < 0:
        l += 1
    elif s > 0:
        r -= 1
    else:
        break
print(*answer,sep=' ')
