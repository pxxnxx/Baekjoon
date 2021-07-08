import sys

n,q = map(int,input().split())
number = dict()
name = dict()

for i in range(n):
    string = sys.stdin.readline().strip()
    number[i] = string
    name[string] = i

for i in range(q):
    question = sys.stdin.readline().strip()
    if question.isdigit() == True:
        print(number[int(question)-1])
    else:
        print(name[question]+1)
