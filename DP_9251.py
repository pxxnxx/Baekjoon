import sys
arr = sys.stdin.readline().strip()
brr = sys.stdin.readline().strip()
o = [[0 for _ in range(len(brr)+1)] for _ in range(len(arr)+1)]
for i in range(1,len(arr)+1):
    for j in range(1,len(brr)+1):
        if arr[i-1] == brr[j-1]:
            o[i][j] = o[i-1][j-1] + 1
        else:
            o[i][j] = max(o[i-1][j],o[i][j-1])
print(o[i][j])
