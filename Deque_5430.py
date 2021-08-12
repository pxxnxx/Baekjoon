import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for i in range(t):
    br = True
    key = input().strip()
    n = int(input())
    a = input().lstrip("[").rstrip("]\n")
    if n == 0:
        arr = deque([])
    else:
        arr = deque(list(map(int,a.split(","))))
    temp = True
    for i in range(len(key)):
        if key[i] == 'R':
            temp = not temp
        elif key[i] == 'D':
            if not arr:
                br = False
                break
            if temp:
                arr.popleft()
            else:
                arr.pop()
    if br:
        if temp and len(arr) > 0:
            print('[',end='')
            for i in range(len(arr)-1):
                print(arr[i],end='')
                print(',',end='')
            print(arr[-1],end='')
            print(']')
        elif not temp and len(arr) > 0:
            print('[',end='')
            for i in range(len(arr)-1):
                print(arr[len(arr)-i-1],end='')
                print(',',end='')
            print(arr[0],end='')
            print(']')
        else:
            print('[]')
    else:
        print('error')
            
        
