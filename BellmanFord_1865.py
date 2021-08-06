import sys
input = sys.stdin.readline

def Bellman(first):
    dist = [sys.maxsize] * (n+1)
    dist[first] = 0
    for i in range(n):
        for start, index, cost in arr:
            if dist[index] > cost + dist[start]:
                dist[index] = cost + dist[start]
                if i == n-1:
                    return True
    return False

t = int(input())
for _ in range(t):
    n, m, w = map(int,input().split())
    arr = []
    for i in range(m):
        start, end, degree = map(int,input().split())
        arr.append((start,end,degree))
        arr.append((end,start,degree))
    for i in range(w):
        start, end, degree = map(int,input().split())
        arr.append((start,end,-degree))
    if Bellman(1):
        print("YES")
    else:
        print("NO")
