import sys

def BFS():
    queue = [1]
    visited[1] = 1
    while queue:
        for i in arr[queue[0]]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = queue[0]
        del queue[0]
n = int(input())
arr = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(n-1):
    x, y = map(int,sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)
BFS()
for i in range(2,n+1):
    print(visited[i])

