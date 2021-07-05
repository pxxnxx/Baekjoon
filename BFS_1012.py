def BFS(x,y):
    queue = []
    queue.append([x,y])
                
    while queue:
        if arr[queue[0][0]][queue[0][1]] == 1:
            for i in range(4):
                xx = queue[0][0] + dx[i]
                yy = queue[0][1] + dy[i]
                if xx >= 0 and yy >= 0 and xx < b and yy < a:
                    if arr[xx][yy] == 1:
                        queue.append([xx,yy])
            arr[queue[0][0]][queue[0][1]] = 0            
        del queue[0]
    

t = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,+1]
for i in range(t):
    a,b,c = map(int,input().split()) # a : - # b : | # c : ea
    cnt = 0
    arr = [[0 for _ in range(a)] for _ in range(b)]
    for j in range(c):
        m,n = map(int,input().split())
        arr[n][m] = 1
    for i in range(b):
        for j in range(a):
            if arr[i][j] == 1:
                BFS(i,j)
                cnt += 1
    print(cnt)
