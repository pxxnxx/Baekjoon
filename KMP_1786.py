def getPS():
    ps = [0] * m
    j = 0
    for i in range(1, m):
        while 0 < j and brr[i] != brr[j]:
            j = ps[j-1]
        if brr[i] == brr[j]:
            j += 1
            ps[i] = j
    return ps

def kmp():
    ps = getPS()
    j = 0
    for i in range(n):
        while 0 < j and arr[i] != brr[j]:
            j = ps[j-1]
        if arr[i] == brr[j]:
            if j == m-1:
                answer.append(i-m+2)
                j = ps[j]
            else:
                j += 1
    return 0

arr = str(input())
brr = str(input())
n = len(arr)
m = len(brr)
answer = []
kmp()
print(len(answer))
print(*answer)
