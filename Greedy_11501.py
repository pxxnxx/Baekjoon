for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    answer = 0 
    m = arr[-1]
    for i in range(n-2,-1,-1):
        if arr[i] > m:
            m = arr[i]
        else:
            answer += m-arr[i]
    print(answer)