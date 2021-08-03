def nqueen(arr,index,n,key):
    brr = arr.copy()
    brr.append(key)
    global answer
    if index == n:
        answer += 1
        return 0
    for i in range(n): # 가로
        for j in range(index): # 세로 
            if brr[j] != i and i != brr[j] + index - j and i != brr[j] + j - index :
                if j == index - 1:
                    nqueen(brr,index+1,n,i)
            else:
                break
n = int(input())
answer = 0
for i in range(n):
    arr = []
    nqueen(arr,1,n,i)
print(answer)


