import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = deque()
for i in range(n):
    a = input().split()
    if a[0] == 'push_front':
        arr.appendleft(int(a[1]))
    elif a[0] == 'push_back':
        arr.append(int(a[1]))
    elif a[0] == 'pop_front':
        if len(arr) != 0:
            print(arr.popleft())
        else:
            print(-1)
    elif a[0] == 'pop_back':
        if len(arr) != 0:
            print(arr.pop())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(arr))
    elif a[0] == 'empty':
        if len(arr) != 0:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if len(arr) != 0:
            print(arr[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if len(arr) != 0:
            print(arr[-1])
        else:
            print(-1)
