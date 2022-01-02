p = [list(map(int,input().split())) for _ in range(3)]
y = p[2][1] - p[0][1]
x = p[1][0] - p[0][0]
l = (p[2][0] - p[0][0]) * (p[1][1] - p[0][1])
if x * y > l:
    print(1)
elif x * y < l:
    print(-1)
else:
    print(0)
