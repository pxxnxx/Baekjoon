from copy import deepcopy
from collections import deque
d = [-1,1,-5,5]
answer = 0
def back(k, vis, v, y, s, b):
    global answer
    vst = deepcopy(vis)
    brr = deepcopy(b)
    brr[k//5][k%5] = 1
    if v == 0:
        vst[k//5][k%5] = 1
        if arr[k//5][k%5] == 'Y':
            y += 1
        else:
            s += 1
        for i in range(k+1, 25):
            back(i, vst, v+1, y, s, brr)
    else:
        if y > 3:
            return
        if v == 6:
            qqq = deque([[k//5, k%5]])
            ret = 0
            dy = [0, 0, -1, 1]
            dx = [1, -1, 0 ,0]
            vvv = [[0 for _ in range(5)] for _ in range(5)]
            vvv[k//5][k%5] = 1
            while qqq:
                yyy, xxx = qqq.popleft()
                for p in range(4):
                    yyyy = yyy + dy[p]
                    xxxx = xxx + dx[p]
                    if 0 <= yyyy < 5 and 0 <= xxxx < 5:
                        if brr[yyyy][xxxx] == 1 and vvv[yyyy][xxxx] == 0:
                            ret += 1
                            qqq.append([yyyy,xxxx])
                            vvv[yyyy][xxxx] = 1
            if ret < 6:
                return

            if y < 3:
                answer += 1
            elif arr[k // 5][k % 5] == 'S':
                answer += 1
            return

        vst[k//5][k%5] = 1
        if arr[k//5][k%5] == 'S':
            s += 1
        else:
            y += 1
        for i in range(k+1, 25):
            back(i, vst, v+1, y, s, brr)

arr = [list(str(input())) for _ in range(5)]
visit = [[0 for _ in range(5)] for _ in range(5)]
brr = [[0 for _ in range(5)] for _ in range(5)]
for i in range(25):
    back(i, visit, 0, 0, 0, brr)
print(answer)