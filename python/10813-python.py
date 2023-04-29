N, M = map(int, input().split())
busket=[]
for a in range(N):
    busket.append(a+1)

for _ in range(M):
    i, j= map(int, input().split())
    busket[i-1], busket[j-1] = busket[j-1], busket[i-1]
    
print(*busket)