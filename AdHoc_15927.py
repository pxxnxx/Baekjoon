def palin(l,r):
    while l < r:
        if s[l] != s[r]:
            return True
        l += 1
        r -= 1
    return False

s = input()
n = len(s)
if palin(0,n-1):
    print(n)
elif palin(0, n-2):
    print(n-1)
else:
    print(-1)

