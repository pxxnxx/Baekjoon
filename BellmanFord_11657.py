import sys
input = sys.stdin.readline

def BF(first):
    dist[first] = 0
    for i in range(n):
        for j in range(m):
            start = arr[j][0]
            index = arr[j][1]
            cost = arr[j][2]
            if dist[start] != sys.maxsize and dist[index] > dist[start] + cost: #갈 수 있는 경우만
                dist[index] = dist[start] + cost
                if i == n-1:
                    return True
    return False

n, m = map(int,input().split())
arr = list()
dist = [sys.maxsize] * (n+1)
for i in range(m):
    start, end, degree = map(int,input().split())
    arr.append((start,end,degree))

if BF(1):
    print("-1")
else:
    for i in range(2,n+1):
        if dist[i] == sys.maxsize:
            print("-1")
        else:
            print(dist[i])
