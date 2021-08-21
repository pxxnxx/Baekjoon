import re
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    if re.compile('(100+1+|01)+').fullmatch(sys.stdin.readline().strip()):
        print("YES")
    else:
        print("NO")
        
    
