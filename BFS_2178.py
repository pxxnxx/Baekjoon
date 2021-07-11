def BFS(x,y):
    cnt = 0
    queue = []
    arr[x][y] = 0
    queue.append([x,y])
    while queue:
        cnt += 1
        for i in range(4):
            xx = queue[0][0] + dx[i]
            yy = queue[0][1] + dy[i]
            if xx >= 0 and yy >= 0 and xx < a and yy < b:
                if arr[xx][yy] != 0:
                    queue.append([xx,yy])
                    arr[xx][yy] = 0
                    ret[xx][yy] = queue[0]    
        del queue[0]
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]
a, b = map(int,input().split())
ret = [[[0,0] for _ in range(b)] for _ in range(a)]
arr = [[0 for _ in range(b)] for _ in range(a)]
for i in range(a):
    st = input()
    for j in range(b):
        arr[i][j] = int(st[j])
BFS(0,0)
n = 0
m = 0
ret[0][0] = [0,0]
a = a-1
b = b-1
c = 1
while a != 0 or b != 0:
    da = a
    a = ret[a][b][0]
    b = ret[da][b][1]
    c += 1
    
print(c)

