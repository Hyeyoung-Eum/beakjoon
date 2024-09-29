MOD = 1000000000

def count_stair_numbers(N):
    dp = [[0] * 10 for _ in range(N + 1)]
    
    #dp[i][j]=길이가 i인 계단 수 중, 마지막 숫자가 j인 경우의 수 저장

    #초기값 : 길이가 1이면, 각각 하나의 계단 수 생성.
    for j in range(1, 10):
        dp[1][j] = 1
    
    #길이가 2 이상이면,
    for i in range(2, N + 1):#2부터 N까지
        for j in range(10): #0~9, 마지막 숫자
            #j=0또는 j=9일때 처리를 위해
            if j > 0:
                #마지막 숫자가 j면 이전 숫자는 j-1.
                dp[i][j] += dp[i-1][j-1]
            if j < 9:
                #마지막 숫자가 j면, 이전 숫자는 j+1
                dp[i][j] += dp[i-1][j+1]
            dp[i][j] %= MOD
    
    #길이에 따라
    result = sum(dp[N]) % MOD
    return result

N = int(input())

# 결과 출력
print(count_stair_numbers(N))









def min_operations_to_one(n):
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        #1을 빼는 연산 : 1을 빼면 1가 i-1이 됨. 결국 i-1을 1로 만드는 연산 횟수를 알고 있으면, 여기에 1을 더하는 것이 됨.
        dp[i] = dp[i - 1] + 1
        #2로 나누어 떨어지면, 둘 중 최솟값. 1을 더해주는 것은 남은 i-1을 1로 만드는 연산 횟수를 더하는 것
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        #3으로 나누어 떨어지면, 둘 중 최솟값.
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[n]

# 입력 받기
n = int(input())

# 결과 출력
print(min_operations_to_one(n))


def min_card_purchase(N, prices):
    #dp[i]는 i개의 카드를 구매할 때 지불해야 하는 금액의 최솟값
    dp = [float('inf')] * (N + 1)
    dp[0] = 0  #0개의 카드를 구매하는 데 드는 비용은 0원

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            dp[i] = min(dp[i], dp[i - j] + prices[j - 1])

    return dp[N]

N = int(input().strip())
prices = list(map(int, input().strip().split()))

print(min_card_purchase(N, prices))
