import sys
input = sys.stdin.readline
n, m = map(int,input().split())
add = dict()
for i in range(n):
    fa, fp = input().split()
    add[fa] = fp
for j in range(m):
    a = input().strip()
    print(add[a])
