import sys
from collections import deque
sys.stdin = open("input.txt")

def Back(y, x, val, per):
    global answer
    if [y, x] in queue:
        answer -= per
        return
    if val == arr[0]:
        return
    queue.appendleft([y, x])
    for i in range(4):
        if arr[i+1] > 0:
            Back(y+dy[i], x+dx[i], val+1, per*arr[i+1])
    queue.popleft()

arr = list(map(int,input().split()))
for i in range(1, 5):
    arr[i] /= 100
queue = deque([[0, 0]])
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
answer = 1
for i in range(4):
    Back(dy[i], dx[i], 1, arr[i+1])
print(answer)