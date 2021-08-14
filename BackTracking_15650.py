def Back(arr,level,index):
    answer = arr.copy()
    answer.append(index)
    if level == m:
        print(*answer)
        return 0
    for i in range(index,n):
        Back(answer,level+1,i+1)

n, m = map(int,input().split())
arr = []
for i in range(n):
    Back(arr,1,i+1)
