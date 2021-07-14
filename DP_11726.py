n = int(input())
s = 0
arr = [1]
for i in range(1,1001):
    arr.append(arr[i-1]*i)
k = n
i = 0
while k >= i:
    s += arr[k] // (arr[k-i] * arr[i])
    i += 1
    k -= 1
print(s%10007)
