import math

n, m = map(int,input().split())
k = int(m ** 0.5)
arr = [1] * (m+1-n)
for i in range(2, k+1):
    start = i**2 * math.ceil(n / i**2)
    if start < m+1:
        for j in range(start, m+1, i**2):
            arr[j-n] = 0
print(sum(arr[:m+1-n]))