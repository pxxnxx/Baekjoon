def BFS(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        for i in arr[queue[0]]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
        print(queue[0],end=' ')
        del queue[0]
   
def DFS(v):
    visit = []
    stack = []
    stack.append(v)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            print(node,end=' ')
            stack.extend(arr[node])
        


n,m,v = map(int,input().split())
arr = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for i in range(m):
    x, y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

for i in range(1,n+1):
    arr[i] = sorted(arr[i],reverse=True)
DFS(v)
print()
for i in range(1,n+1):
    arr[i] = sorted(arr[i])
BFS(v)
