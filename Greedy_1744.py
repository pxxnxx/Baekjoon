import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = deque(sorted([int(input()) for _ in range(n)],reverse=True))
answer = 0
while arr:
    a = arr.pop()
    if arr:
        b = arr.pop()
        if a <= 0 and b <= 0:
            answer += a*b
        else:
            arr.append(b)
            arr.append(a)
            break
    else:
        arr.append(a)
        break
while arr:
    a = arr.popleft()
    if arr:
        b = arr.popleft()
        if a + b <= a*b:
            answer += a*b
        else:
            arr.append(b)
            answer += a
    else:
        answer += a
print(answer)
