import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for i in range(n):
    arr.append(list(map(int,list(input().strip()))))
def dac(a,b,c):
    br = 0
    key = arr[a][b]
    for i in range(a,a+c):
        for j in range(b,b+c):
            if key != arr[i][j]:
                br = 1
                break
        if br == 1:
            break
    if br == 1:
        print('(',end='')
        dac(a,b,c//2)
        dac(a,b+c//2,c//2)
        dac(a+c//2,b,c//2)
        dac(a+c//2,b+c//2,c//2)
        print(')',end='')
    else:
        print(key,end='')

dac(0,0,n)    
