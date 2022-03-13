import sys
input = sys.stdin.readline

n, k, s = map(int,input().split())
prr = []
nrr = []
for _ in range(n):
    a, b = map(int,input().split())
    if a > s:
        prr.append([a, b])
    else:
        nrr.append([a, b])
prr.sort(key=lambda x:abs(x[0]-s),reverse=True)
nrr.sort(key=lambda x:abs(x[0]-s),reverse=True)
i = 0
answer = 0
while i < len(prr):
    dist = abs(prr[i][0]-s) * 2
    for _ in range(k):
        prr[i][1] -= 1
        if prr[i][1] == 0:
            i += 1
        if i >= len(prr):
            break
    answer += dist
i = 0
while i < len(nrr):
    dist = abs(nrr[i][0]-s) * 2
    for _ in range(k):
        nrr[i][1] -= 1
        if nrr[i][1] == 0:
            i += 1
        if i >= len(nrr):
            break
    answer += dist
print(answer)