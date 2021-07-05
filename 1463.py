x = int(input())
arr = []
for i in range(1000001):
    arr.append(i-1)
for i in range(2,1000001):
    if i%3 == 0 and arr[i//3]+1 < arr[i]:
        arr[i] = arr[i//3] + 1
    if i%2 == 0 and arr[i//2]+1 < arr[i]:
        arr[i] = arr[i//2] + 1
    if arr[i-1]+1 < arr[i]:
        arr[i] = arr[i-1] + 1
print(arr[x])
