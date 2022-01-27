import sys
input = sys.stdin.readline

def find(num):
    if root[num] != num:
        return find(root[num])
    else:
        return num

n = int(input())
m = int(input())
root = [i for i in range(n+1)]
arr = sorted([list(map(int,input().split())) for _ in range(m)],key=lambda x:x[2])
answer = 0

for s, e, w in arr:
    sr = find(s)
    er = find(e)
    if sr != er:
        if sr > er:
            root[sr] = er
        else:
            root[er] = sr
        answer += w
print(answer)