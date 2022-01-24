from collections import deque
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(a, index, v):
    visit[index] = 1
    for x in a[index]:
        if visit[x] == 0:
            dfs(a, x, v)
    if v == 0:
        stack.append(index)

t = int(input())
ret = []
for _ in range(t):
    n, m = map(int,input().split())
    arr = [[] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    stack = []
    for _ in range(m):
        a, b = map(int,input().split())
        arr[a].append(b)
    queue = deque()
    answer = 0

    for i in range(1, n+1):
        if visit[i] == 0:
            dfs(arr, i, 0)
    visit = [0 for _ in range(n+1)]
    while stack:
        index = stack.pop()
        if visit[index] == 0:
            dfs(arr, index, 1)
            answer += 1
    ret.append(answer)
print(*ret, sep='\n')
