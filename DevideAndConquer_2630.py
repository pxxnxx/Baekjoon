import sys
input = sys.stdin.readline
n = int(input())
arr = list()
for i in range(n):
    arr.append(list(map(int,input().split())))
answer = [0,0]
def daq(a,b,c):
    key = arr[a][b]
    br = 0
    if c == 1:
        answer[arr[a][b]] += 1
        return 0
    for i in range(a,a+c):
        for j in range(b,b+c):
            if arr[i][j] != key:
                daq(a,b,c//2)
                daq(a,b+c//2,c//2)
                daq(a+c//2,b,c//2)
                daq(a+c//2,b+c//2,c//2)
                br = 1
                break
        if br == 1:
            break
    if br == 0:
        answer[key] += 1
daq(0,0,n)
print(answer[0])
print(answer[1])
