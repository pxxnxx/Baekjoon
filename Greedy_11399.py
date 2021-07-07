n = int(input())
arr = list(map(int,input().split()))
s = 0

arr = sorted(arr)
for i in range(n):
    s += (n-i)*arr[i]
print(s)
