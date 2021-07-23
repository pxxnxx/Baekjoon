import sys
def BFS(x):
    queue = []
    queue.append(x)
    while queue:
        for i in arr[queue[0]]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
        del queue[0]
n,m = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)
cnt = 0
for i in range(1,n+1):
    if visited[i] == 0:
        k =BFS(i)
        #if k > 0:
        cnt += 1
print(cnt)
