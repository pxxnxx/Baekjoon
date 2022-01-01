import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, k = map(int,input().split())
arr = sorted([list(map(int,input().split())) for _ in range(n)])
bag = sorted([int(input()) for _ in range(k)])

answer = 0
select = []
j = 0
for i in range(k):
    while j < n and bag[i] >= arr[j][0]:
        heappush(select, -arr[j][1])
        j += 1
    if select:
        answer += -heappop(select)
print(answer)