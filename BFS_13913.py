import sys
def BFS(x,y):
    queue = [x,]
    visited[x] = 1
    while queue:
        for i in arr[queue[0]]:
            if i == y:
                ret[i] = queue[0]
                return visited[queue[0]]
            if i<100001 and visited[i] == 0: 
                queue.append(i)
                visited[i] = visited[queue[0]]+1
                ret[i] = queue[0]
        del queue[0]

n,k = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(100001)]
visited = [0] * 100001
ret = [-1] * 100001
arr[0].append(1)
for i in range(1,100001):
    arr[i].append(i-1)
    arr[i].append(i+1)
    arr[i].append(i*2)
answer = []
if n<k:
    print(BFS(n,k))
    answer = []
    while k != -1:
        answer = [k] + answer
        k = ret[k]
else:
    print(n-k)
    for i in range(n, k-1, -1):
        answer.append(i)
print(*answer,sep=' ')

