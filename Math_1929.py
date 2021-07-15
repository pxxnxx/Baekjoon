m,n = map(int,input().split())

def er(x):
    br = 0
    if x == 1:
        br = 1
    for i in range(2,int(x**0.5+1)):
        if x != i and x % i == 0:
            br = 1
            break
    if br == 0:
        print(x)

for i in range(m,n+1):
    er(i)    
