'''
4 3
1 2 3 4
'''
n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
answer = 0
i = 0
while i < n:
    j = i+1
    while j < n:
        if arr[j] - arr[i] <= m - 1:
            j += 1
        else:
            break
    answer += 1
    i = j
print(answer)
