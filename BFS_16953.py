from collections import deque
a, b = map(int,input().split())
queue = deque([[a,1]])
re = True
while queue:
    x, y = queue.popleft()
    if x == b:
        re = False
        print(y)
    if x*2 <= b:
        queue.append([x*2,y+1])
    if x*10+1 <= b:
        queue.append([x*10+1,y+1])
if re:
    print("-1")
