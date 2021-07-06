n,c = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
def GetCount(distance):
    count = 1 # first home
    current = arr[0]
    for i in range(1,n):
        if distance <= arr[i] - current:
            current = arr[i]
            count += 1
    return count
def BS(c):
    start = 1 # minimum distance
    end = arr[-1] - arr[0] # maximum distance
    while start <= end:
        mid = (start + end) // 2
        if GetCount(mid) < c:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    print(answer)
BS(c)
