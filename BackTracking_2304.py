n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr = sorted(arr)
m = 0
for i in range(n):
    m = max(m, arr[i][1])
s = 0
l = 0
q = arr[0][0]
p = arr[0][1]
while l < n:
    if arr[l][1] > p:
        s += p * (arr[l][0] - q)
        q = arr[l][0]
        p = arr[l][1]
    if arr[l][1] == m:
        break
    l += 1
r = n-1
q = arr[n-1][0]
p = arr[n-1][1]
while r > 0:
    if arr[r][1] > p:
        s += p * (q - arr[r][0])
        q = arr[r][0]
        p = arr[r][1]
    if arr[r][1] == m:
        break
    r -= 1
s += (arr[r][0]-arr[l][0]+1) * m
print(s)