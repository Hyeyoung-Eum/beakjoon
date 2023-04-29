N, M = map(int, input().split())

basket = list(range(1,N+1))

for _ in range(M):
    i, j = map(int, input().split())

    #원래 내 풀이 : 지우고 가장 맨 앞 인덱스에다가 삽입
    for a in basket[i-1:j]:
        basket.remove(a)
        basket.insert(i-1, a)

    ###다른 풀이
    # temp = basket[i-1:j]
    # temp.reverse()
    # basket[i-1:j] = temp

print(*basket)