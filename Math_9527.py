def solution(a):
    ret = 0
    n = 0
    while 2**n < a+1:
        ret += 2**n * ((a+1) // 2**n // 2)
        if (a+1) // 2**n % 2 == 1:
            ret += (a+1) % 2**n
        n += 1
    return ret
n, m = map(int,input().split())
print(solution(m)-solution(n-1))






# 12 = 1100
# m // 2^n * 2^n-1
# m -> 0 1 2 3 4 5 6 7 8 9 0 1 2
# 0 -> 0 1 0 1 0 1 0 1 0 1 0 1 0 => 6 / 1 1
# 1 -> 0 0 1 1 0 0 1 1 0 0 1 1 0 => 6 / 2 2
# 2 -> 0 0 0 0 1 1 1 1 0 0 0 0 1 => 5 / 4 4
# 3 -> 0 0 0 0 0 0 0 0 1 1 1 1 1 => 5 / 8 8

# 8 // 4 => 2 / 2블럭 4 * (2//2)
# 10 // 4 => 2 / 2블럭 4 * (2//2)
# 10 // 8 => 1 / 1블럭 8 * (1//2) + 11 % 8 (홀수 일때만)
# 6 // 4 => 1 / 1블럭 4 * (1//2) + 7 % 4