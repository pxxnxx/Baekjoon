import sys
input = sys.stdin.readline
n = int(input())
tree = dict()
for i in range(n):
    name, left, right = input().split()
    tree[name] = name,left,right
def a(tr):
    print(tree[tr][0],end='')
    if tree[tr][1] != '.':
        a(tree[tr][1])
    if tree[tr][2] != '.':
        a(tree[tr][2])
def b(tr):
    if tree[tr][1] != '.':
        b(tree[tr][1])
    if tree[tr][2] != '.':
        b(tree[tr][2])
    print(tree[tr][0],end='')
def c(tr):
    if tree[tr][1] != '.':
        c(tree[tr][1])
    print(tree[tr][0],end='')
    if tree[tr][2] != '.':
        c(tree[tr][2])

a('A')
print()
c('A')
print()
b('A')
print()
