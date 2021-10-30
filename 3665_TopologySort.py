import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    deg = [0] * n
    after = [0] * n
    for i in range(n):
        deg[arr[i]-1] = n-i-1
    m = int(input())
    for _ in range(m):
        a, b = map(int,input().split())
        a -= 1
        b -= 1
        if deg[a] > deg[b]:
            after[a] -= 1
            after[b] += 1
        else:
            after[a] += 1
            after[b] -= 1
    for i in range(n):
        deg[i] += after[i]
    answer = []
    b = 0
    for i in range(1, n+1):
        temp = []
        for j in range(n):
            if deg[j] == n-i:
                if temp:
                    b = 1
                    break
                temp.append(j+1)
                deg[j] = -1
        if b:
            break
        if not temp:
            b = 1
            break
        answer.append(temp[0])
    if b:
        print("IMPOSSIBLE")
    else:
        print(*answer,sep=' ')