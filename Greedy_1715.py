import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    heappush(arr,int(input()))
answer = 0
while len(arr) > 1:
    a = heappop(arr)
    b = heappop(arr)
    answer += a+b
    heappush(arr, a+b)
print(answer)
