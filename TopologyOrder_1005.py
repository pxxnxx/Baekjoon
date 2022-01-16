import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
p = []
for _ in range(t):
    n, k = map(int,input().split())
    degree = [0 for _ in range(n+1)]
    arr = [[] for _ in range(n+1)]
    time = [0] + list(map(int,input().split()))
    answer = [0 for _ in range(n+1)]
    for i in range(k):
        start, end = map(int,input().split())
        degree[end] += 1
        arr[start].append(end)
    queue = deque([])

    for i in range(1, n+1):
        if degree[i] == 0:
            queue.append(i)
            answer[i] = time[i]
    while queue:
        index = queue.popleft()
        for x in arr[index]:
            degree[x] -= 1
            answer[x] = max(answer[index] + time[x], answer[x])
            # 0 되자마자 넣어야 함.
            if degree[x] == 0:
                queue.append(x)
    w = int(input())
    p.append(answer[w])
print(*p,sep='\n')