n = int(input())
arr = [input() for _ in range(n)]
val = [[0, i] for i in range(26)]
num = [i for i in range(10)]
ret = [0] * 26
for i in range(n):
    for j in range(len(arr[i])):
        asc = ord(arr[i][j]) - 65
        val[asc][0] += 10 ** (len(arr[i]) - j - 1)
val.sort(reverse=True, key=lambda x:x[0])
for i in range(26):
    if val[i][0] == 0:
        break
    ret[val[i][1]] = num.pop()
answer = 0
for i in range(n):
    for j in range(len(arr[i])):
        asc = ord(arr[i][j]) - 65
        answer += ret[asc] * 10 ** (len(arr[i]) - j - 1)
print(answer)