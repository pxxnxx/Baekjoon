
# TODO
#   갯수 셀 때는 j = ps[j] 필수

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
    global answer
    ps = getPS()
    j = 0
    for i in range(n):
        while 0 < j and arr[i] != brr[j]:
            j = ps[j-1]
        if arr[i] == brr[j]:
            if j == m-1:
                answer += 1
                j = ps[j]
            else:
                j += 1

def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


m = int(input())
arr = list(map(str,input().split()))
brr = list(map(str,input().split()))
arr = arr + arr[:m-1]
n = len(arr)
answer = 0
kmp()
g = gcd(answer, m)
print(answer // g ,"/", m // g, sep='')