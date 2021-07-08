import sys
import heapq
heapp = []
heapn = []
n = int(sys.stdin.readline())
for i in range(n):
    k = int(sys.stdin.readline())
    if k == 0:
        if heapp or heapn:
            if heapp and heapn:
                if heapp[0] < heapn[0]:
                    print(heapq.heappop(heapp))
                else:
                    print(-(heapq.heappop(heapn)))
            elif heapp:
                print(heapq.heappop(heapp))
            else:
                print(-(heapq.heappop(heapn)))
        else:
            print(0)
    elif k > 0:
        heapq.heappush(heapp,k)
    else:
        heapq.heappush(heapn,-k)
