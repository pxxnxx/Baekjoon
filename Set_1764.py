import sys
input = sys.stdin.readline
arr = set()
brr = set()
a, b = map(int,input().split())
for i in range(a):
    arr.add(input().strip())
for i in range(b):
    brr.add(input().strip())
answer = sorted(list(arr&brr))
print(len(answer))
for i in range(len(answer)):
    print(answer[i])
