from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
time = [0 for _ in range(n+1)]
deg = [0 for _ in range(n+1)]
arr = [[] for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
for i in range(1, n+1):
    inp = list(map(int,input().split()))
    time[i] = inp[0]
    answer[i] = inp[0]
    for j in range(2, inp[1]+2):
        arr[i].append(inp[j])
        deg[inp[j]] += 1
queue = deque()
for i in range(1, n+1):
    if deg[i] == 0:
        queue.append(i)
while queue:
    index = queue.popleft()
    for x in arr[index]:
        deg[x] -= 1
        answer[x] = max(answer[index] + time[x], answer[x])
        if deg[x] == 0:
            queue.append(x)
print(max(answer))
