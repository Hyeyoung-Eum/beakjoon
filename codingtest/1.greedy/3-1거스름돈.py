n=1200
count=0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin #해당 coin으로 거슬러줄 수 있는 동전 개수 세기
    n %= coin #남은 금액

print(count)