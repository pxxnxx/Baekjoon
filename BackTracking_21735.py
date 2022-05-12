def Back(time, index, value):
    global answer
    value += arr[index]
    if time == m:
        answer = max(answer, value)
        return
    if index == n-1:
        answer = max(answer,value)
        return
    if index+1 < n:
        Back(time+1, index+1, value)
    if index+2 < n:
        Back(time+1, index+2, value//2)

n, m = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0
Back(1, 0, 1)
if n > 1:
    Back(1, 1, 0)
print(answer)