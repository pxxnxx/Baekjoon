import heapq
import sys
heap = []
n = int(sys.stdin.readline())
for i in range(n):
    k = int(sys.stdin.readline())
    if k != 0:
        heapq.heappush(heap,(-k,k))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
