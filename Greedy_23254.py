import sys
from heapq import heappop, heappush
sys.stdin = open("input.txt")
input = sys.stdin.readline

while True:
    try:
        n, m = map(int,input().split())
        n *= 24
        score = list(map(int,input().split()))
        plus = list(map(int,input().split()))
        heap = []
        for i in range(m):
            if score[i] + plus[i] > 100:
                plus[i] = 100 - score[i]
            heappush(heap,[-plus[i], score[i]])

        time = 0
        while time < n:
            p, s = heappop(heap)
            s -= p
            if s - p > 100:
                p = s - 100
            heappush(heap, [p, s])
            time += 1
        answer = 0
        for i in range(m):
            answer += heap[i][1]
        print(answer)

    except:
        break