'''
4
4 4
5 2
11 5
15 10
25 10
'''


import sys
from heapq import heappop, heappush
sys.stdin = open("input.txt")
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        arr = sorted([list(map(int,input().split())) for _ in range(n)])
        end, stock = map(int,input().split())
        start = 0
        l = 0
        answer = 0
        heap = []
        while start+stock < end:
            for i in range(l, len(arr)):
                if arr[i][0] > start + stock:
                    break
                l = i+1
                heappush(heap, [-arr[i][1]] + arr[i])
            if not heap and start+stock < end:
                answer = -1
                break
            next = heappop(heap)
            stock += start - next[1] + next[2]
            start = next[1]
            answer += 1
        print(answer)
    except:
        break



# for _ in range(n):
#     dist, oil = map(int,input().split())
#     heappush(heap,[-oil, dist, oil])
# end, stock = map(int,input().split())
# answer = 0
# start = 0
# while start + stock < end:
#     push = []
#     while heap:
#         edge = heappop(heap)
#         if edge[1] <= start + stock:
#             answer += 1
#             stock += start - edge[1] + edge[2]
#             start = edge[1]
#             break
#         push.append(edge)
#     if heap:
#         for x in push:
#             if x[1] > start:
#                 heappush(heap, x)
#     elif start + stock < end:
#         answer = -1
#         break

# print(answer)
'''
5
1 5
5 7
6 1
7 10
8 3
20 10
'''