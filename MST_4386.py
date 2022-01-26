import sys
input = sys.stdin.readline

def find(num):
    if root[num] == num:
        return num
    else:
        return find(root[num])

n = int(input())
arr = [list(map(float, input().split())) for _ in range(n)]
root = [i for i in range(n)]
edge = []
for i in range(n-1):
    for j in range(i+1, n):
        edge.append([i,j,((arr[j][0] - arr[i][0]) ** 2 + (arr[j][1] - arr[i][1]) ** 2) ** 0.5])
edge = sorted(edge, key=lambda x:x[2])
answer = 0
for start, end, weight in edge:
    sroot = find(start)
    eroot = find(end)
    if sroot != eroot:
        if sroot > eroot:
            root[sroot] = eroot
        else:
            root[eroot] = sroot
        answer += weight
print(round(answer, 2))
