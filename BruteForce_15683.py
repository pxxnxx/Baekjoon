import sys
answer = sys.maxsize
from copy import deepcopy
def watch(brr, q, v):
    global answer
    if v == len(q):
        s = 0
        for i in range(len(brr)):
            for j in range(len(brr[0])):
                if brr[i][j] == 0:
                    s += 1
        if answer > s:
            answer = s
        # print(*brr,'',sep='\n')
        return
    # print(v, q[v][0], q[v][1])
    y = queue[v][0]
    x = queue[v][1]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    if queue[v][2] == 1:
        for i in range(4):
            vec = i
            arr = deepcopy(brr)
            yy = y
            xx = x
            while 0 <= yy < n and 0 <= xx < m:
                if arr[yy][xx] == 0:
                    arr[yy][xx] = -1
                elif arr[yy][xx] == 6:
                    break
                yy += dy[vec]
                xx += dx[vec]
            watch(arr, q, v+1)
    elif queue[v][2] == 2:
        for i in range(2):
            vec = i
            arr = deepcopy(brr)
            for _ in range(2):
                yy = y
                xx = x
                while 0 <= yy < n and 0 <= xx < m:
                    if arr[yy][xx] == 0:
                        arr[yy][xx] = -1
                    elif arr[yy][xx] == 6:
                        break
                    yy += dy[vec]
                    xx += dx[vec]
                vec = (vec + 2) % 4
            watch(arr, q, v+1)

    elif queue[v][2] == 3:
        for i in range(4):
            vec = i
            arr = deepcopy(brr)
            for _ in range(2):
                yy = y
                xx = x
                while 0 <= yy < n and 0 <= xx < m:
                    if arr[yy][xx] == 0:
                        arr[yy][xx] = -1
                    elif arr[yy][xx] == 6:
                        break
                    yy += dy[vec]
                    xx += dx[vec]
                vec = (vec + 1) % 4
            watch(arr, q, v+1)


    elif queue[v][2] == 4:
        for i in range(4):
            vec = i
            arr = deepcopy(brr)
            for _ in range(3):
                yy = y
                xx = x
                while 0 <= yy < n and 0 <= xx < m:
                    if arr[yy][xx] == 0:
                        arr[yy][xx] = -1
                    elif arr[yy][xx] == 6:
                        break
                    yy += dy[vec]
                    xx += dx[vec]
                vec = (vec + 1) % 4
            watch(arr, q, v+1)

    elif queue[v][2] == 5:
        vec = 1
        arr = deepcopy(brr)
        for _ in range(4):
            yy = y
            xx = x
            while 0 <= yy < n and 0 <= xx < m:
                if arr[yy][xx] == 0:
                    arr[yy][xx] = -1
                elif arr[yy][xx] == 6:
                    break
                yy += dy[vec]
                xx += dx[vec]
            vec = (vec + 1) % 4
        watch(arr, q, v+1)

    return arr, v+1


if __name__ == '__main__':
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    queue = []
    for i in range(n):
        for j in range(m):
            if 0 < arr[i][j] < 6:
                queue.append([i,j,arr[i][j]])
    watch(arr, queue, 0)
    print(answer)