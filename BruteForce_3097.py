import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
now = [0, 0]
for x, y in arr:
    now[0] += x
    now[1] += y
print(*now, sep=' ')
m = sys.maxsize
for x, y in arr:
    m = min(m, ((now[0]-x)**2 + (now[1]-y)**2) ** 0.5)
print("{0:.2f}".format(m))

