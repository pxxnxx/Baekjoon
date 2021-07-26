from math import gcd
x, y = map(int,input().split())
print(y-gcd(x,y))
