# TODO
#   코드 이따구로 짠 거 고칠 것
#   유의사항 :
#       - 0 도 문자 취급
#       - Z 는 변환 X, input 받을 순 있음
#       - K = 36 인데 모든 문자 안 바뀐 경우 있었음, += 1 로 처리 했음



def sti(num):
    num = ord(num)
    if 48 <= num < 58:
        num -= 48
    elif 65 <= num <= 90:
        num -= 55
    return num

def its(num):
    if 0 <= num < 10:
        num = chr(num+48)
    elif 10 <= num < 36:
        num = chr(num+55)
    return num

n = int(input())
arr = [list(str(input())) for _ in range(n)]
k = int(input())
key = [[i, 0] for i in range(91)]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        m = sti(arr[i][len(arr[i])-j-1])
        key[ord(arr[i][len(arr[i])-j-1])][1] += 36 ** j * (m + 1)
key.sort(key=lambda x:x[1],reverse=True)
Z = [0] * 91
profit = [[i, 0] for i in range(91)]
i = 0
while True:
    if key[i][1] == 0:
        break
    # if sti(chr(key[i][0])) == 0:
    #     profit[key[i][0]][1] = 36
    # else:
    profit[key[i][0]][1] = 36 * key[i][1] // (sti(chr(key[i][0]))+1) - key[i][1]
    i += 1
for i in range(48,58):
    profit[i][1] += 1
for i in range(65,90):
    profit[i][1] += 1
profit[90][1] = 0
profit.sort(key=lambda x:x[1], reverse=True)
for i in range(k):
    Z[profit[i][0]] = 1

s = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if Z[ord(arr[i][j])] == 1:
            arr[i][j] = 'Z'
        s += 36 ** (len(arr[i])-j-1) * sti(arr[i][j])
i = 0
answer = []
while s:
    answer = [its(s % 36)] + answer
    s //= 36
if answer:
    print(*answer,sep='')
else:
    print(0)

'''
10
ASDFJH
ADSFKAF
DSJFFD
23JH4
2J4H32
23JH
LK65
L6KN3
LKN22
LKN
0
'''