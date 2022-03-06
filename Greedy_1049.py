import sys

n, m = map(int,input().split())
b, s = sys.maxsize, sys.maxsize
for _ in range(m):
    x, y = map(int,input().split())
    b = min(b, x)
    s = min(s, y)
num = 0
answer = 0
while num < n:
    if n - num > 6:
        if 6 * s > b:
            answer += b
            num += 6
        else:
            answer += (n - num) * s
            num = n
    else:
        if (n - num) * s > b:
            answer += b
            num += 6
        else:
            answer += (n - num) * s
            num = n
print(answer)

