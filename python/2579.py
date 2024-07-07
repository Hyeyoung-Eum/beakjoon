import sys

input = sys.stdin.readline

N=int(input())

#계단의 숫자를 초기화. 1층은 1번째 인덱스에 저장
stairs = [0]*301
for i in range(1, N+1):
    stairs[i] = int(input())

#dp 배열을 초기화
dp = [0]* 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

#점화식 계산
for i in range(4, N+1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

print(dp[N])