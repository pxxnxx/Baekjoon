import sys
input = sys.stdin.readline
n = int(input())
arr = []
dpM = [[0,0,0]]
dpm = [[0,0,0]]
for i in range(n):
    arr.append(list(map(int,input().split())))
    M0 = max(dpM[0][0],dpM[0][1]) + arr[0][0]
    M1 = max(dpM[0][0],dpM[0][1],dpM[0][2]) + arr[0][1]
    M2 = max(dpM[0][1],dpM[0][2]) + arr[0][2]
    m0 = min(dpm[0][0],dpm[0][1]) + arr[0][0]
    m1 = min(dpm[0][0],dpm[0][1],dpm[0][2]) + arr[0][1]
    m2 = min(dpm[0][1],dpm[0][2]) + arr[0][2]
    dpM.append([M0,M1,M2])
    dpm.append([m0,m1,m2])
    del arr[0]
    del dpM[0]
    del dpm[0]
print(max(dpM[0][0],dpM[0][1],dpM[0][2]),min(dpm[0][0],dpm[0][1],dpm[0][2]))

