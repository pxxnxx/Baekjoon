from collections import deque
n, m = map(int,input().split())
visit = [0 for _ in range(100001)]
answer = [0 for _ in range(100001)]
queue = deque([n])
while queue:
    i = queue.popleft()
    if i == m:
        break
    # 시간 0이라 가장 먼저 실행해야 함
    if i*2 <= 100000:
        if visit[i*2] == 0:
            answer[i*2] = answer[i]
            visit[i*2] = 1
            queue.append(i*2)
        elif answer[i*2] > answer[i]:
            answer[i*2] = answer[i]
            queue.append(i*2)
    if i-1 >= 0:
        if visit[i-1] == 0:
            answer[i-1] = answer[i] + 1
            visit[i-1] = 1
            queue.append(i-1)
        elif answer[i-1] > answer[i] + 1:
            answer[i-1] = answer[i] + 1
            queue.append(i-1)
    if i+1 <= 100000:
        if visit[i+1] == 0:
            answer[i+1] = answer[i] + 1
            visit[i+1] = 1
            queue.append(i+1)
        elif answer[i+1] > answer[i] + 1:
            answer[i+1] = answer[i] + 1
            queue.append(i+1)

print(answer[m])

