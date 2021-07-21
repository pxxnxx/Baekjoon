x, y = map(int,input().split())
arr = []
s = 0
for i in range(1,47):
    for j in range(i):
        arr.append(i)
for i in range(x-1,y):
    s += arr[i]
print(s)
