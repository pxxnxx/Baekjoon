n, r, c = map(int,input().split())
sn = 2 ** n
key = 0
def daq(a,b,c):
    global key
    if c == 1:
        return 0
    if a < c // 2 and  b < c // 2:
        daq(a,b,c-c//2)
    elif a < c // 2 and b >= c // 2:
        key += c**2 // 4
        daq(a,b-c//2,c-c//2)
    elif a >= c//2 and b < c // 2:
        key += 2 * c**2 // 4
        daq(a-c//2,b,c-c//2)
    else:
        key += 3 * c**2 // 4
        daq(a-c//2,b-c//2,c-c//2)
daq(r,c,sn)
print(key)
