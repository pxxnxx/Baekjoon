import sys
input = sys.stdin.readline
n = int(input())
s = 0
answer = [1 for _ in range(1001)]
arr = list(map(int,input().split()))
for i in arr:
    br = 0
    if i == 1:
        br = 1
    for j in range(2,int(i**0.5+1)):
        if j != i and i % j == 0:
            br = 1
            break
    if br == 0:
        s += 1
print(s)
