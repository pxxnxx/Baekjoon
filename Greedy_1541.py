arr = input().split('-')
br = list()
for i in arr:
    inbr = 0
    red = i.split('+')
    for j in red:
        inbr += int(j)
    br.append(inbr)
answer = br[0]
for i in range(1,len(br)):
    answer -= br[i]
print(answer)
