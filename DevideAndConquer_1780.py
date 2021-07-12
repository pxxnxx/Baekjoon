import sys
input = sys.stdin.readline
arr = list()
answer = [0,0,0]
n = int(input())
for i in range(n):
    arr.append(list(map(int,input().split())))

def rec(a,b,c):
    key = arr[a][b]
    br = 0
    for i in range(a,a+c):
        for j in range(b,b+c):
            if key != arr[i][j]:
                br = 1
                break
            else:
                br = 0
        if br == 1:
            break
    if br == 1:
        rec(a,b,c//3)
        rec(a,b+c//3,c//3)
        rec(a,b+2*c//3,c//3)
                    
        rec(a+c//3,b,c//3)
        rec(a+c//3,b+c//3,c//3)
        rec(a+c//3,b+2*c//3,c//3)
                    
        rec(a+2*c//3,b,c//3)
        rec(a+2*c//3,b+c//3,c//3)
        rec(a+2*c//3,b+2*c//3,c//3)
    else:
        answer[key+1] +=1
rec(0,0,n)
print(answer[0])
print(answer[1])
print(answer[2])
