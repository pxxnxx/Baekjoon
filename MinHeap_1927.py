import heapq
import sys
n = int(sys.stdin.readline())
heap = []
for i in range(n):
    k = int(sys.stdin.readline())
    if k == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,k)
