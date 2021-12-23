import sys
input = sys.stdin.readline
arr = []
for i in range(4):
    arr.append(input().strip())
state = [0, 0, 0, 0]
n = int(input())
for i in range(n):
    num, val = map(int,input().split())
    num -= 1
    next_state = []
    for j in range(3):
        if num+j+1 > 3:
            break
        if arr[num+j][(state[num+j]+2)%8] != arr[num+j+1][(state[num+j+1]-2)%8]:
            next_state.append([num+j+1, (state[num+j+1] + ((-1) ** (j+2) * val)) % 8])
        else:
            break
    for j in range(3):
        if num-j-1 < 0:
            break
        if arr[num-j][(state[num-j]-2)%8] != arr[num-j-1][(state[num-j-1]+2)%8]:
            next_state.append([num-j-1, (state[num-j-1] + ((-1) ** (j+2) * val)) % 8])
        else:
            break
    state[num] = (state[num] - val) % 8
    while next_state:
        state[next_state[0][0]] = next_state[0][1]
        del next_state[0]
s = 0
for i in range(4):
    s += 2 ** i * int(arr[i][state[i]])
print(s)