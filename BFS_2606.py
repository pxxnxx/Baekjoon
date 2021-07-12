def BFS(start):
    queue = []
    c = 0
    queue.append(start) # 1
    visited[start] = 1
    while queue:
        for i in arr[queue[0]]: #
            if visited[i] == 0:
                queue.append(i) # queue -> 1 2 5
                visited[i] = 1
                c += 1
        del queue[0]    
    print(c)

n = int(input())
k = int(input())
arr = [[]for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for i in range(k):
    x, y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
    
BFS(1)
