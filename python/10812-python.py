N, M= map(int, input().split())
basket=[]
for _ in range(N):
    basket.append(_+1)

for __ in range(M):
    i, j, k = map(int, input().split())
    
    temp_basket=basket[k:j+1]
    for a in basket[i:k+1]:
        temp_basket.append(a)
    basket[i:j+1]=temp_basket
    print(basket)

print(*basket)