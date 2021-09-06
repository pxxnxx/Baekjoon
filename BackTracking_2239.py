import sys
input = sys.stdin.readline
def comp(i,j,k):
    for a in range(9):
        if arr[a][j] == k:
            return False
        elif arr[i][a] == k:
            return False
    for a in range(i//3*3, i//3*3+3):
        for b in range(j//3*3, j//3*3+3):
            if arr[a][b] == k:
                return False
    return True

def Back(key):
    if key == 81:
        for c in range(9):
            for r in range(9):
                print(arr[c][r],end='')
            print()
        sys.exit()
    i = key//9
    j = key%9
    if arr[i][j] != 0:
        Back(key+1)
    else:
        for a in range(1,10):
            if comp(i,j,a):
                arr[i][j] = a
                Back(key+1)
        if a == 9:
            arr[i][j] = 0
            return
if __name__ == '__main__':                
    arr = list()
    for i in range(9):
        arr.append(list(map(int,input().strip())))
    Back(0)
    
