def Back(sum, index):
    global answer
    sum += arr[index]
    if sum == m:
        answer += 1
    if index == n-1:
        return

    for i in range(index+1, n):
        Back(sum, i)

n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
answer = 0
for i in range(n):
    Back(0, i)
print(answer)