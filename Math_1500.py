n, m = map(int,input().split())
answer = 1
while m != 0:
    answer *= n // m
    n -= n//m
    m -= 1
print(answer)
