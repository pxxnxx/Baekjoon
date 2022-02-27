n = int(input())
arr = list(map(int,input().split()))
stack = [0]
answer = [-1 for _ in range(n)]
for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
print(*answer,sep=' ')