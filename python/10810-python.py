#바구니 문제
N, M = map(int, input().split())

#리스트 만들고, 0으로 채워넣기 원래 코드
# busket=[]
# for a in range(N):
#     busket.append(0)

#리스트 만들고, 0으로 채워넣기 개선 코드
busket = [0]*N

for b in range(M):
    i, j, k = map(int, input().split())

    for c in range(i-1,j):
        busket[c]=k

print(*busket)
