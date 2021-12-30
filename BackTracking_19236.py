from copy import deepcopy
answer = 0
def fish(brr, crr, a, s):
    global answer
    if a > answer:
        answer = a
    arr = deepcopy(brr)
    mp = deepcopy(crr)
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    live = [0 for _ in range(16)]
    for i in range(4):
        for j in range(4):
            if mp[i][j] >= 0:
                live[mp[i][j]] = 1
    i = 0
    limit = 0
    while i < len(arr):

        if limit == 8:
            i += 1
            limit = 0
        y, x, v = arr[i][0], arr[i][1], arr[i][2]
        if live[i] == 0:
            i += 1
            limit = 0
            continue
        if 0 <= y + dy[v] < 4 and 0 <= x + dx[v] < 4:
            if mp[y+dy[v]][x+dx[v]] >= 0:
                next = mp[y+dy[v]][x+dx[v]]

                temp = arr[next][0], arr[next][1]
                arr[next][0], arr[next][1] = y, x
                arr[i][0], arr[i][1] = temp
                mp[y+dy[v]][x+dx[v]] = i
                mp[y][x] = next
                i += 1
                limit = 0
            elif mp[y+dy[v]][x+dx[v]] == -1:
                arr[i][0] = y+dy[v]
                arr[i][1] = x+dx[v]
                mp[y+dy[v]][x+dx[v]] = i
                mp[y][x] = -1
                i += 1
                limit = 0

            else:
                arr[i][2] = (arr[i][2] + 1) % 8
                limit += 1
        else:
            arr[i][2] = (arr[i][2] + 1) % 8
            limit += 1
    shark(s, arr, mp, a)

def shark(s, brr, crr, a):
    arr = deepcopy(brr)
    mp = deepcopy(crr)
    y = arr[s][0]
    x = arr[s][1]
    v = arr[s][2]
    mp[y][x] = -1
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    p = 0
    for i in range(3):
        y += dy[v]
        x += dx[v]
        # print(y,x)
        if 0 <= y < 4 and 0 <= x < 4 and mp[y][x] >= 0:
            temp = mp[y][x]
            mp[y][x] = -2
            fish(arr,mp,a+temp+1, temp)
            mp[y][x] = temp
            p += 1

if __name__ == '__main__':
    inp = [list(map(int,input().split())) for _ in range(4)]
    arr = [[0,0,0] for _ in range(16)]
    for i in range(4):
        k = inp[i]
        for j in range(4):
            k[2*j] -= 1
            arr[k[2*j]][0], arr[k[2*j]][1], arr[k[2*j]][2] = i, j, k[2*j+1]-1
        del inp[i][7]
        del inp[i][5]
        del inp[i][3]
        del inp[i][1]
    a = inp[0][0]
    inp[0][0] = -2
    fish(arr, inp, a+1, a)
    print(answer)
