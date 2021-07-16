n = int(input())
answer = 0
for i in range(1,101):
    if 5 * i <= n:
        answer += 1
    else:
        break
for i in range(1,21):
    if 25 * i <= n:
        answer += 1
    else:
        break
for i in range(1,5):
    if 125*i <= n:
        answer += 1
    else:
        break
print(answer)
