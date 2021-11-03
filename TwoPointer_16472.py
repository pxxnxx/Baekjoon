import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
def sti(num):
    return int(ord(cat[num])-97)
while True:
    try:
        n = int(input())
        cat = str(input().strip())
        if len(cat) <= n:
            print(len(cat))
        else:
            answer = 0
            check = [0] * 26
            l = 0
            r = 1
            check[sti(l)] += 1
            var = 1
            if check[sti(r)] == 0:
                var += 1
            check[sti(r)] += 1
            temp = 2
            r += 1
            while r < len(cat):
                if check[sti(r)] == 0:
                    var += 1
                check[sti(r)] += 1
                temp += 1
                while var > n:
                    check[sti(l)] -= 1
                    if check[sti(l)] == 0:
                        var -= 1
                    l += 1
                    temp -= 1
                r += 1

                answer = max(answer, temp)
            print(answer)
    except:
        break
