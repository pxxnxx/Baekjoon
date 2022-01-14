import sys
from copy import deepcopy
input = sys.stdin.readline
answer = sys.maxsize
answer_arr = []
def handle(put, q, aarr, index, value):
    global answer
    global answer_arr
    arr = deepcopy(put)
    queue = deepcopy(q)
    arar = deepcopy(aarr)
    arar.append(value)
    n_queue = []
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    b, r, change = 0, 0, 0
    if index > 10:
        return
    while queue:
        y = queue[0][0]
        yy = y + dy[value]
        x = queue[0][1]
        xx = x + dx[value]
        v = arr[queue[0][0]][queue[0][1]]
        if arr[yy][xx] == '.':
            arr[yy][xx] = v
            arr[y][x] = '.'
            queue[0][0] = yy
            queue[0][1] = xx
        elif arr[yy][xx] == '#':
            n_queue.append([y, x])
            del queue[0]
        elif arr[yy][xx] == 'O':
            if v == 'B':
                b = 1
            elif v == 'R':
                r = 1
            arr[y][x] = '.'
            del queue[0]
        elif arr[yy][xx] == 'R' or arr[yy][xx] == 'B':
            if change == 0:
                queue.append([y, x])
                change = 1
            if change == 1:
                n_queue.append([y, x])
            del queue[0]
    if b == 1:
        return
    elif r == 1:
        if answer > index:
            answer = index
            answer_arr = arar
        return
    else:
        handle(arr, n_queue, arar, index+1, (value+1) % 4)
        handle(arr, n_queue, arar, index+1, (value+3) % 4)

if __name__ == '__main__':
    n, m = map(int,input().split())
    inp = [list(input().strip()) for _ in range(n)]
    que = []
    for i in range(n):
        for j in range(m):
            if inp[i][j] == 'R' or inp[i][j] == 'B':
                que.append([i,j])
    for i in range(4):
        handle(inp, que, [], 1, i)
    trans = ['R', 'D', 'L', 'U']
    if answer < sys.maxsize:
        for i in range(answer):
            answer_arr[i] = trans[answer_arr[i]]
        print(answer, ' ',*answer_arr, sep='')
    else:
        print(-1)