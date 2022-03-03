import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = list(map(int,input().split()))
s = [0]
for i in range(n):
    s.append(s[i] + arr[i])
answer = sys.maxsize
l = 0
r = 1
while l < n:
    if s[r] - s[l] < m:
        if r < n:
            r += 1
        else:
            l += 1
    else:
        answer = min(answer, r-l)
        l += 1

if answer == sys.maxsize:
    print(0)
else:
    print(answer)