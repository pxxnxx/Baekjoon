from collections import deque
n = int(input())
queue = deque([n])
count = [1000000 for _ in range(1000001)]
count[n] = 0
fpr = [-1] * 1000001
fpr[n] = n
while queue:
    x = queue.popleft()
    if x == 1:
        break
    if x%3 == 0 and count[x//3] > count[x] + 1:
        queue.append(x//3)
        count[x//3] = count[x] + 1
        fpr[x//3] = x
    if x%2 == 0 and count[x//2] > count[x] + 1:
        queue.append(x//2)
        count[x//2] = count[x] + 1
        fpr[x//2] = x
    if count[x-1] > count[x] + 1:
        queue.append(x-1)
        count[x-1] = count[x] + 1
        fpr[x-1] = x
print(count[1])
key = 1
arr = []
while key != n:
    arr.append(key)
    key = fpr[key]
arr.append(key)
while arr:
    print(arr.pop(),end=' ')
