from copy import deepcopy
def brute(c, p):
    brr = deepcopy(c)
    for y, x in p:
        brr[y][x] = 1
    queue = []
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    ret = 0
    visit = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if brr[i][j] == 2:
                queue.append([i, j])
                visit[i][j] = 1
    while queue:
        y, x = queue[0]
        del queue[0]
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < n and 0 <= xx < m and brr[yy][xx] == 0 and visit[yy][xx] == 0:
                queue.append([yy, xx])
                visit[yy][xx] = 1
                brr[yy][xx] = 1
    for i in range(n):
        for j in range(m):
            if brr[i][j] == 0:
                ret += 1
    return ret

def solution(n, m, arr):
    l = n * m
    answer = 0
    for i in range(l):
        y1, x1 = i // m, i % m
        if arr[y1][x1] != 0:
            continue
        for j in range(i+1, l):
            y2, x2 = j // m, j % m
            if arr[y2][x2] != 0:
                continue
            for k in range(j+1, l):
                y3, x3 = k // m, k % m
                if arr[y3][x3] != 0:
                    continue
                answer = max(answer, brute(arr, [[y1,x1],[y2,x2],[y3,x3]]))
    return answer

if __name__ == '__main__':
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    print(solution(n, m, arr))