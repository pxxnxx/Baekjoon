import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))

def Back(key,index, number):
    answer = key.copy()
    answer.append(arr[number])
    if index == m-1:
        print(*answer)
        return 0
    for i in range(n):
        if arr[i] not in answer:
            Back(answer,index+1,i)
        
for i in range(n):
    key = []
    Back(key,0,i)
