import sys
def check(num):
    if root[num] == num:
        return num
    return check(root[num])

input = sys.stdin.readline
n, m = map(int,input().split())
s = [''] + list(map(str,input().strip().split()))
root = [i for i in range(n+1)]
arr = sorted([list(map(int,input().split())) for _ in range(m)],key=lambda x:x[2])

answer = 0
for start, end, cost in arr:
    if s[start] == s[end]:
        continue
    sroot, eroot = check(start), check(end)
    if sroot != eroot:
        if sroot < eroot:
            root[eroot] = sroot
        else:
            root[sroot] = eroot
        answer += cost
first = check(1)
for i in range(2, n+1):
    if first != check(i):
        answer = -1
        break
print(answer)
