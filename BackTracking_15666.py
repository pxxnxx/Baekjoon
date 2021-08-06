import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = sorted(list(set(map(int,input().split()))))
n = len(arr)
def Back(key,index, number):
    answer = key.copy()
    answer.append(arr[number])
    if index == m-1:
        print(*answer)
        return 0
    for i in range(number,n):
        Back(answer,index+1,i)
        
for i in range(n):
    key = []
    Back(key,0,i)
