n = int(input())
a = [False, False] + [True] * (n-1)
p = []
for i in range(2, n+1):
    if a[i]:
        p.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

answer = 1
for i in range(len(p)):
    s = p[i]
    while s <= n:
        prev = s
        s *= p[i]
    answer *= prev
    answer %= 987654321
print(answer)