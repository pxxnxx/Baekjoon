def BS(start,end,n):
    while start <= end:
        mid = (start + end) // 2
        answer = 0
        for i in arr:
            answer += i // mid
        if answer >= n:
            start = mid + 1
        else:
            end = mid - 1
    return end
k,n = map(int,input().split())
arr = list()
for i in range(k):
    arr.append(int(input()))
print(BS(1,max(arr),n))

