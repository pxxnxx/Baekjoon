import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = list()
answer = 0
s = 0
for i in range(n):
    arr.append(int(input()))
while i >= 0:
    if s == k:
        break
    if s+arr[i] <= k:
        s += arr[i]
        answer += 1
    else:
        i -= 1
print(answer)
