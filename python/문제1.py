N, K = map(int, input().split())

num=0

while(N!=1):
    if N>=K:
        N=N//K
        num+=1
    else:
        N=N-1
        num+=1

print(num)
