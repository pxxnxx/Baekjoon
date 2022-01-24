import sys
input = sys.stdin.readline

def find(num):
    if parent[num] == num:
        return num
    else:
        return find(parent[num])

v, e = map(int,input().split())
parent = [i for i in range(v+1)]
answer = 0
edge = sorted([list(map(int,input().split())) for _ in range(e)], key=lambda x:x[2])
for start, end, weight in edge:
    sr = find(start)
    er = find(end)
    if sr != er:
        if sr > er:
            parent[sr] = er
        else:
            parent[er] = sr
        answer += weight
print(answer)