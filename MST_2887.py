import sys
input = sys.stdin.readline

def find(num):
    if root[num] == num:
        return num
    else:
        return find(root[num])

n = int(input())
arr = [[_] + list(map(int,input().split())) for _ in range(n)]
edge = []
root = [i for i in range(n+1)]

# 복습
for i in range(1,4):
    arr.sort(key=lambda x:x[i])
    for j in range(n-1):
        edge.append([arr[j][0], arr[j+1][0], abs(arr[j][i]-arr[j+1][i])])

edge.sort(key=lambda x:x[2])
answer = 0
for s, e, w in edge:
    sr = find(s)
    er = find(e)
    if sr != er:
        if sr > er:
            root[sr] = er
        else:
            root[er] = sr
        answer += w
print(answer)