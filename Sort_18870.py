import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
brr = list()
for i in range(n):
    brr.append([arr[i],i])
brr.sort()
key = 0
s = brr[0][0] - 1
for i in range(n):
    if s == brr[i][0]:
        key -= 1
    s = brr[i][0]
    brr[i][0] = key
    key += 1
brr.sort(key = lambda x : x[1])
for i in range(n):
    print(brr[i][0],end=' ')
