import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    answer = 1
    arr = dict()
    n = int(input())
    for i in range(n):
        f = input().split()
        if f[1] not in arr.keys():
            arr[f[1]] = 2
        else:
            arr[f[1]] += 1
    for x in arr.values():
        answer *= x
    print(answer-1)
