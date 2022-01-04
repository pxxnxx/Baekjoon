import sys
def move(shark):
    for i in range(len(shark)):
        if shark[i][0] == -1:
            continue
        k = 0
        sp = shark[i][2]
        if 0 < shark[i][3] <= 2:
            if r != 1:
                sp %= 2*(r-1)
            else:
                sp = 0
        else:
            if c != 1:
                sp %= 2*(c-1)
            else:
                sp = 0
        while k != sp:
            if shark[i][3] == 1:
                if 0 <= shark[i][0] - 1:
                    shark[i][0] -= 1
                    k += 1
                else:
                    shark[i][3] = 2
            elif shark[i][3] == 2:
                if shark[i][0] + 1 < r:
                    shark[i][0] += 1
                    k += 1
                else:
                    shark[i][3] = 1
            elif shark[i][3] == 3:
                if shark[i][1] + 1 < c:
                    shark[i][1] += 1
                    k += 1
                else:
                    shark[i][3] = 4
            elif shark[i][3] == 4:
                if 0 <= shark[i][1] - 1:
                    shark[i][1] -= 1
                    k += 1
                else:
                    shark[i][3] = 3
    return shark

def check(shark):
    mpp = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(len(shark)):
        if shark[i][0] == -1:
            continue
        if mpp[shark[i][0]][shark[i][1]] == 0:
            mpp[shark[i][0]][shark[i][1]] = shark[i][4]
        else:
            if mpp[shark[i][0]][shark[i][1]] < shark[i][4]:
                for j in range(len(shark)):
                    if shark[j][4] == mpp[shark[i][0]][shark[i][1]] and shark[j][0] != -1:
                        mpp[shark[i][0]][shark[i][1]] = shark[i][4]
                        shark[j][0] = -1
                        break
            elif mpp[shark[i][0]][shark[i][1]] > shark[i][4]:
                shark[i][0] = -1
    return shark, mpp

def fishing(fisher, shark, mp):
    for i in range(len(mp)):
        if mp[i][fisher] != 0:
            break
    if mp[i][fisher] == 0:
        return 0, shark
    for j in range(len(shark)):
        if shark[j][4] == mp[i][fisher] and shark[j][1] == fisher:
            shark[j][0] = -1
            shark[j][1] = -1
            break
    return shark[j][4], shark

if __name__ == '__main__':
    input = sys.stdin.readline
    r, c, m = map(int,input().split())
    shark = [list(map(int,input().split())) for _ in range(m)]
    test = [-1 for _ in range(10001)]
    mp = [[0 for _ in range(c)] for _ in range(r)]
    for x in shark:
        x[0] -= 1
        x[1] -= 1
    answer = 0
    for i in range(c):
        shark, mp = check(shark)
        point, shark = fishing(i, shark, mp)
        answer += point
        shark = move(shark)
    print(answer)