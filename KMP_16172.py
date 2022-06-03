

# TODO
#   j = ps[j-1] 인것 유의
#   j = ps[j] 아님


def getPS():
    j = 0
    ps = [0] * m
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
                return 1
            else:
                j += 1
    return 0

a = str(input())
arr = []
brr = str(input())
for i in range(len(a)):
    if 47 < ord(a[i]) < 58:
        continue
    arr.append(a[i])
n = len(arr)
m = len(brr)
print(kmp())