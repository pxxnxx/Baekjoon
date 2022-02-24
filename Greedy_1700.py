# 3 6
# 1 3 5
# 2 -> 1 out
# 4 -> 3 out
# 6 -> 5 out
# => 꽉 차있을 때 들어오는 숫자보다 작은 수 중 가장 큰 수
from collections import deque
n, m = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(m):
    arr[i] -= 1
print(arr)
on = [0 for _ in range(m)]
answer = 0
i = 0
queue = deque()
while len(queue) < n:
    if arr[i] not in queue:
        queue.append(arr[i])
        i += 1
while queue:
    x = queue.popleft()
    on[x] = 1
while len(queue) < n:
    if arr[i] not in queue:
        queue.append(arr[i])
        i += 1
while queue:
    x = queue.popleft()
    if on[x] == 1:
        continue
    for j in range(i, m):
        if arr[j] not in queue:
            queue.append(arr[j])
            i = j + 1
            break
    for j in range(m):
        print(j, on[j], queue)
        if on[j] == 1 and j not in queue:
            on[j] = 0
            on[x] = 1
            print("on", x, "off", arr[j])
            answer += 1
            break
print(answer)