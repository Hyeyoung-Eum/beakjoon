def convert_to_base(n, b):
    #0이면 0리턴
    if n == 0:
        return "0"
    
    digits = []

    while n:
        #divmod로 몫과 나머지 동시 반환
        n, remainder = divmod(n, b)
        #나머지가 10이상이면, 알파벳을 대문자로 추가
        if remainder >= 10:
            digits.append(chr(ord('A') + remainder - 10))
        else:
            digits.append(str(remainder))
    
    return ''.join(digits[::-1])

N, B = map(int, input().strip().split())

print(convert_to_base(N, B))

def count_ways(n):
    #dp[11]까지 가능하도록
    dp = [0] * 12
    #안쓰는 방법은 1가지
    dp[0] = 1 

    for i in range(1, 12):
        #dp[i]= i를 1,2,3들의 합으로 나타내는 방법의 수
        
        #i-1수에다가 1을 더하거나, i-2수에다가 모두 2를 더하거나, i-3수에다가 모두 3을 더하는 경우임
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        if i - 3 >= 0:
            dp[i] += dp[i - 3]
    
    return dp[n]

# 입력 받기
T = int(input().strip())
test_cases = [int(input().strip()) for _ in range(T)]

# 각 테스트 케이스에 대해 결과 출력
for case in test_cases:
    print(count_ways(case))

MOD = 1000000009

def count_ways(n):
    if n == 1:
        return 1  #1
    if n == 2:
        return 1  #2
    if n == 3:
        return 2  #1+2 3

    dp = [[0] * 4 for _ in range(n + 1)]
    
    #dp[i][j]=j를 마지막으로 끝나는 i를 만드는 경우의 수,
    dp[1][1] = 1  #1
    dp[2][1] = 1  #1+1
    dp[2][2] = 1  #2
    dp[3][1] = 1  #2+1
    dp[3][2] = 1  #1+2
    dp[3][3] = 1  #3

    for i in range(4, n + 1):
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MOD #1로 끝나려면, 이전에 2나 3으로 끝나야함
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MOD #2로 끝나려면, 이전에 1나 3으로 끝나야함
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MOD #3로 끝나려면, 이전에 1나 2로 끝나야함

    return (dp[n][1] + dp[n][2] + dp[n][3]) % MOD

# 입력 받기
T = int(input().strip())
test_cases = [int(input().strip()) for _ in range(T)]

# 각 테스트 케이스에 대해 결과 출력
for case in test_cases:
    print(count_ways(case))


MOD = 1000000009
MAX_N = 100000

def preprocess():
    dp = [[0] * 4 for _ in range(MAX_N + 1)]
    
    dp[1][1] = 1 #1
    dp[2][2] = 1 #2
    dp[3][1] = 1 #2+1
    dp[3][2] = 1 #1+2
    dp[3][3] = 1 #3

    for i in range(4, MAX_N + 1):
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MOD #1로 끝나려면, 이전에 2나 3으로 끝나야함
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MOD #2로 끝나려면, 이전에 1나 3으로 끝나야함
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MOD #3로 끝나려면, 이전에 1나 2로 끝나야함

    #결과 저장
    results = [0] * (MAX_N + 1)
    for i in range(1, MAX_N + 1):
        results[i] = (dp[i][1] + dp[i][2] + dp[i][3]) % MOD

    return results

results = preprocess()

T = int(input().strip())
test_cases = [int(input().strip()) for _ in range(T)]

for case in test_cases:
    print(results[case])

