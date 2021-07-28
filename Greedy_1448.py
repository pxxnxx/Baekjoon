import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list([int(input()) for _ in range(n)]),reverse=True)
while True:
    if len(arr) < 3:
        print(-1)
        break
    if arr[0] < arr[1] + arr[2]:
        print(arr[0]+arr[1]+arr[2])
        break
    else:
        del arr[0]
