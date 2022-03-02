n = int(input())
m = int(n ** 0.5)
prime = [True] * (n+1)
arr = []
for i in range(2, m + 1):
    if prime[i]:
        for j in range(i*2, n+1, i):
            prime[j] = False

for i in range(2, n+1):
    if prime[i]:
        arr.append(i)

answer = 0
for i in range(len(arr)):
    s = 0
    for j in range(i, len(arr)):
        s += arr[j]
        if s > n:
            break
        elif s == n:
            answer += 1
            break
print(answer)

# for i in range(len(arr)-1):
#     l = i
#     r = len(arr) - 1
#     while l <= r:
#         num += 1
#         if arr[r] - arr[l] < n:
#             break
#         elif arr[r] - arr[l] > n:
#             r -= 1
#         else:
#             answer += 1
#             break
# print(num)
# print(time.time() - start)