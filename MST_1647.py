def find(num):
    if root[num] == num:
        return num
    else:
        return find(root[num])

n, m = map(int,input().split())
edge = sorted([list(map(int,input().split())) for _ in range(m)], key=lambda x:x[2])
root = [i for i in range(n+1)]
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
        last = w
print(answer-last)
