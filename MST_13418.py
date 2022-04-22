import sys
sys.stdin = open("input.txt")

def find(num):
    if root[num] == num:
        return num
    return find(root[num])

input = sys.stdin.readline

n, m = map(int,input().split())
arr = sorted([list(map(int,input().split())) for _ in range(m+1)], key=lambda x:x[2], reverse=True)
root = [i for i in range(n+1)]
min = 0
for start, end, cost in arr:
    sroot, eroot = find(start), find(end)
    if sroot != eroot:
        if sroot < eroot:
            root[eroot] = sroot
        else:
            root[sroot] = eroot
        if cost == 0:
            min += 1

arr = sorted(arr, key=lambda x:x[2])
root = [i for i in range(n+1)]
max = 0
for start, end, cost in arr:
    sroot, eroot = find(start), find(end)
    if sroot != eroot:
        if sroot < eroot:
            root[eroot] = sroot
        else:
            root[sroot] = eroot
        if cost == 0:
            max += 1
print(max**2 - min**2)
