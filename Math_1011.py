t = int(input())
p = []
for _ in range(t):
    start, end = map(int,input().split())
    dist = end - start
    s = 0
    a = 1
    answer = 1
    while True:
        s += a
        if s >= dist:
            p.append(answer)
            break
        answer += 1

        s += a
        if s >= dist:
            p.append(answer)
            break
        answer += 1
        a += 1
print(*p, sep='\n')