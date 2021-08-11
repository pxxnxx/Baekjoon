def func(k,m):
    cnt = 0
    if k <= m:
        cnt += 1
        cnt += func(k*10+4,m)
        cnt += func(k*10+7,m)
    return cnt

a,b = map(int,input().split())
print(func(0,b)-func(0,a-1))
