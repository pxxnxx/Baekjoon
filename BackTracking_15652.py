n, m = map(int,input().split())
def Back(key,index,number):
    answer = key.copy()
    answer.append(number)
    if index == m:
        print(*answer)
        return 0
    for i in range(number,n+1):
        Back(answer,index+1,i)

for i in range(1,n+1):
    key = []
    Back(key,1,i)
