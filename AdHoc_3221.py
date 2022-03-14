import sys
input = sys.stdin.readline

l, t = map(int,input().split())
n = int(input())
loc = []
vec = []

for _ in range(n):
    a, b = map(str, input().split())
    loc.append(int(a))
    if b == 'L':
        vec.append(-1)
    else:
        vec.append(1)

for i in range(n):
    loc[i] += vec[i] * t
    while loc[i] > l or loc[i] < 0:
        if loc[i] > l:
            loc[i] = 2*l - loc[i]
        elif loc[i] < 0:
            loc[i] = -loc[i]
        vec[i] = -vec[i]

print(*sorted(loc),sep=' ')