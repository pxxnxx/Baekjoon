import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
s = [arr[0]]
for i in range(1,n):
    s.append(arr[i]+s[i-1])
for i in range(m):
    a,b = map(int,input().split())
    if a == 1:
        print(s[b-1])
    else:
        print(s[b-1]-s[a-2])
