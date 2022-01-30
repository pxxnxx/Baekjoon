import sys
input = sys.stdin.readline

def find(num):
    if root[num] == num:
        return num
    else:
        return find(root[num])
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    edge = sorted([list(map(int,input().split())) for _ in range(m)], key=lambda x:x[2])
    root = [i for i in range(n)]
    answer = 0
    for i in range(m):
        answer += edge[i][2]
    for s, e, w in edge:
        sr = find(s)
        er = find(e)
        if sr != er:
            if sr > er:
                root[sr] = er
            else:
                root[er] = sr
            answer -= w
    print(answer)

